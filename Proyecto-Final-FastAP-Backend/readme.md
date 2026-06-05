# Backend (FastAPI)

Este directorio contiene el código del servidor FastAPI, que actúa como la API para la aplicación, gestionando la lógica de negocio y la integración con Keycloak para la autenticación y CockroachDB para la auditoría.

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

### Configuración de CockroachDB (Auditoría)

Para que el sistema de auditoría funcione, debes crear la base de datos y la tabla en CockroachDB:

1.  **Accede a la consola de CockroachDB:**
    ```bash
    cockroach sql --url "postgresql://root@192.168.64.2:26257?sslmode=disable"
    ```

2.  **Ejecuta los siguientes comandos SQL:**
    ```sql
    CREATE DATABASE laboratorio_db;
    USE laboratorio_db;

    CREATE TABLE login_events (
        id SERIAL PRIMARY KEY,
        username STRING NOT NULL,
        event_type STRING NOT NULL,
        timestamp TIMESTAMP DEFAULT current_timestamp()
    );
    ```

### Inicio del Servicio Backend

Para que la API sea accesible desde la red de la VM, ejecútala escuchando en todas las interfaces (`0.0.0.0`):

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Este comando iniciará el servidor FastAPI en `http://192.168.64.2:8000/api`.

