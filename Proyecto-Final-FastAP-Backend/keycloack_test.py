from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from security import keycloak_openid, get_current_user

app = FastAPI()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # Se eliminó la coma al final
        token = keycloak_openid.token(
            form_data.username,
            form_data.password
        )
        return token
    except Exception as e:
        # Se cambió 'code' por 'status_code' y se añadió el error al detalle
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Credenciales inválidas o error de conexión: {str(e)}"
        )
    
@app.get("/perfil")
def obtener_perfil(usuario_actual: dict = Depends(get_current_user)):  
    """
    Esta ruta está protegida. Solo se puede acceder si FastAPI 
    valida el token JWT a través de Keycloak.
    """  
    return {
        "mensaje": "¡Autenticación exitosa!",
        "datos_del_usuario": usuario_actual
    }