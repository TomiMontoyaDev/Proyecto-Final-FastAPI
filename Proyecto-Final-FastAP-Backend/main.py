from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from security import keycloak_openid, get_current_user, keycloak_admin
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

app = FastAPI(
    title="Mi API con Keycloak",
    root_path="/api"
)

# --- CONFIGURACIÓN COCKROACHDB ---
DB_URL = "postgresql://root@192.168.64.2:26257/laboratorio_db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo de auditoría
class LoginEvent(Base):
    __tablename__ = "login_events"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    event_type = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Función inyectora (Llamar después del registro exitoso)
def inject_login_event(username: str, event: str = "REGISTER_SUCCESS"):
    db = SessionLocal()
    try:
        new_log = LoginEvent(username=username, event_type=event)
        db.add(new_log)
        db.commit()
    finally:
        db.close()
# ---------------------------------

# Modelo de datos para Login
class UserLogin(BaseModel):
    username: str
    password: str

# Modelo de datos para Registro
class UserRegister(BaseModel):
    username: str
    password: str
    email: str = None

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.64.2",
        "http://localhost:5173"     
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LOGIN: Se comunica con Keycloak para obtener el token
@app.post("/login")
async def login(data: UserLogin):
    try:
        # Obtenemos el token desde Keycloak usando las credenciales del usuario
        token = keycloak_openid.token(
            username=data.username,
            password=data.password
        )
        
        # Registrar evento de login exitoso en CockroachDB
        inject_login_event(data.username, "LOGIN_SUCCESS")

        # Retornamos el token y el username para que el frontend lo guarde
        return {
            "access_token": token["access_token"],
            "refresh_token": token["refresh_token"],
            "expires_in": token["expires_in"],
            "username": data.username,
            "message": "Login exitoso"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Credenciales inválidas o error de conexión con Keycloak: {str(e)}"
        )

# REGISTER: Crea un usuario en Keycloak usando la API de Administración
@app.post("/register")
async def register(user: UserRegister):
    try:
        # 1. Crear el usuario en Keycloak
        new_user = keycloak_admin.create_user({
            "email": f"{user.username}@example.com",
            "username": user.username,
            "enabled": True,
            "emailVerified": True,
            "requiredActions": [],
            "credentials": [{
                "value": user.password,
                "type": "password",
                "temporary": False
            }],
        }, exist_ok=False)

        # Registrar evento de registro exitoso en CockroachDB
        inject_login_event(user.username, "REGISTER_SUCCESS")

        return {
            "message": "Usuario registrado correctamente en Keycloak",
            "username": user.username,
            "id": new_user
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al registrar usuario en Keycloak: {str(e)}"
        )

# Ruta protegida de ejemplo
@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Has accedido a una ruta protegida",
        "user_info": current_user
    }

@app.get("/")
def read_root():
    return {"message": "API de Hardsoft con FastAPI y Keycloak activa"}