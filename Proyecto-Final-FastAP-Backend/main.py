from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from security import keycloak_openid, get_current_user

app = FastAPI()

# Modelo de datos para Login
class UserLogin(BaseModel):
    username: str
    password: str

# Modelo de datos para Registro (Si decides manejarlo localmente o via Keycloak API)
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

# REGISTER: Ejemplo simple (Normalmente Keycloak maneja esto, pero puedes usar su API Admin)
@app.post("/register")
async def register(user: UserRegister):
    # Aquí deberías integrar la creación de usuario en Keycloak usando keycloak_admin
    # Por ahora, solo simulamos una respuesta exitosa
    return {
        "message": "Usuario registrado correctamente (Simulado)",
        "username": user.username
    }

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
