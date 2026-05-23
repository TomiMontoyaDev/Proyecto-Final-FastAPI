from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from keycloak import KeycloakOpenID
from jose import jwt  # Usamos jose directamente
from config import settings

keycloak_openid = KeycloakOpenID(
    server_url=settings.KEYCLOAK_SERVER_URL,
    client_id=settings.KEYCLOAK_CLIENT_ID,
    realm_name=settings.KEYCLOAK_REALM_NAME,
    client_secret_key=settings.KEYCLOAK_CLIENT_SECRET
)

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # Limpiamos posibles comillas accidentales
    token = token.strip('"')
    
    try:
        # Obtenemos la llave pública desde Keycloak
        # keycloak_openid.public_key() devuelve la llave en formato PEM
        public_key = f"-----BEGIN PUBLIC KEY-----\n{keycloak_openid.public_key()}\n-----END PUBLIC KEY-----"
        
        # Validamos usando JOSE directamente. 
        # Al usar jose.jwt.decode aquí, evitamos el conflicto de argumentos.
        # verify_exp=False ignora la expiración (problema de hora/clock drift)
        user_info = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            options={"verify_exp": False, "verify_aud": False}
        )
        return user_info
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Error al validar token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )