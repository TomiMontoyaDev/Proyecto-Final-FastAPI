# Backend (FastAPI)

Este directorio contiene el código del servidor FastAPI, que actúa como la API para la aplicación, gestionando la lógica de negocio y la integración con Keycloak para la autenticación.

## Configuración y Dependencias

Sigue estos pasos para configurar y levantar el servicio backend.

### Rutas y Preparación

1.  **Navega a este directorio:**
    ```bash
    cd Proyecto-Final-FastAP-Backend
    ```

2.  **Crea y activa un entorno virtual (si aún no lo has hecho):**
    ```bash
    python3 -m venv venv
    # En macOS/Linux:
    source venv/bin/activate
    # En Windows:
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura las variables de entorno para Keycloak:**
    Asegúrate de tener un archivo `.env` en este mismo directorio (`Proyecto-Final-FastAP-Backend`) con las siguientes variables:
    ```
    KEYCLOAK_SERVER_URL=TU_URL_DE_KEYCLOAK_SERVER
    KEYCLOAK_REALM_NAME=TU_NOMBRE_DE_REALM
    KEYCLOAK_CLIENT_ID=TU_CLIENT_ID
    KEYCLOAK_CLIENT_SECRET=TU_CLIENT_SECRET
    ```
    Reemplaza los valores con la configuración de tu instancia de Keycloak.

### Inicio del Servicio Backend

Desde este directorio (`Proyecto-Final-FastAP-Backend`) y con el entorno virtual activado, ejecuta:

```bash
uvicorn main:app --reload --port 8000
```
Este comando iniciará el servidor FastAPI en `http://127.0.0.1:8000` con recarga automática.
