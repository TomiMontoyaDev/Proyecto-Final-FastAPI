from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    KEYCLOAK_SERVER_URL:str
    KEYCLOAK_REALM_NAME:str
    KEYCLOAK_CLIENT_ID:str
    KEYCLOAK_CLIENT_SECRET:str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()