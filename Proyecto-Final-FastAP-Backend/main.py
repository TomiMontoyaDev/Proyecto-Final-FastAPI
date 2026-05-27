from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from security import keycloak_openid, get_current_user, keycloak_admin

app = FastAPI()

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
    allow_origins=["http://localhost:5173"],
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
        # Nota: El cliente en Keycloak debe tener roles de 'manage-users' en Service Account Roles
        # o estar configurado para permitir la creación.
        new_user = keycloak_admin.create_user({
            "email": f"{user.username}@example.com",
            "username": user.username,
            "enabled": True,
            "emailVerified": True,
            "requiredActions": [],        # ← fuerza lista vacía
            "credentials": [{
                "value": user.password,
                "type": "password",
                "temporary": False
            }],
        }, exist_ok=False)

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
