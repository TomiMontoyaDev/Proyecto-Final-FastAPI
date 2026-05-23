# Proyecto Final FastAPI con React y Keycloak

Este proyecto es una aplicación web full-stack que integra un backend desarrollado con FastAPI y un frontend con React, utilizando Keycloak para la autenticación y gestión de usuarios.

## Estructura del Proyecto

El proyecto se divide en dos componentes principales:

-   `Proyecto-Final-FastAP-Backend/`: Contiene el código del servidor FastAPI.
-   `Proyecto-Final-FastAPI-Frontend/`: Contiene el código de la aplicación cliente React.

## Configuración del Entorno y Dependencias

Sigue estos pasos para configurar y levantar ambos servicios.

### 1. Backend (FastAPI)

#### Rutas y Preparación

1.  **Navega al directorio del backend:**
    ```bash
    cd Proyecto-Final-FastAP-Backend
    ```

2.  **Crea y activa un entorno virtual:**
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
    Asegúrate de tener un archivo `.env` en el directorio `Proyecto-Final-FastAP-Backend` con las siguientes variables:
    ```
    KEYCLOAK_SERVER_URL=TU_URL_DE_KEYCLOAK_SERVER
    KEYCLOAK_REALM_NAME=TU_NOMBRE_DE_REALM
    KEYCLOAK_CLIENT_ID=TU_CLIENT_ID
    KEYCLOAK_CLIENT_SECRET=TU_CLIENT_SECRET
    ```
    Reemplaza los valores con la configuración de tu instancia de Keycloak.

#### Inicio del Servicio Backend

Desde el directorio `Proyecto-Final-FastAP-Backend` y con el entorno virtual activado, ejecuta:

```bash
uvicorn main:app --reload --port 8000
```
Este comando iniciará el servidor FastAPI en `http://127.0.0.1:8000` con recarga automática.

### 2. Frontend (React)

#### Rutas y Preparación

1.  **Abre una nueva terminal** y navega al directorio del frontend:
    ```bash
    cd Proyecto-Final-FastAPI-Frontend
    ```

2.  **Instala las dependencias de Node.js:**
    ```bash
    npm install
    # O si usas yarn:
    yarn install
    ```

#### Inicio del Servicio Frontend

Desde el directorio `Proyecto-Final-FastAPI-Frontend`, ejecuta:

```bash
npm run dev
```
Este comando iniciará el servidor de desarrollo de React, generalmente en `http://localhost:5173`.

## Secuencia de Inicio

Para que la aplicación funcione correctamente, es crucial iniciar los servicios en el siguiente orden:

1.  **Inicia el Backend (FastAPI)**.
2.  **Inicia el Frontend (React)**.

Una vez que ambos servicios estén ejecutándose, podrás acceder a la aplicación en tu navegador (normalmente `http://localhost:5173`) y probar la funcionalidad de login con Keycloak.

## Prueba de Login

1.  Abre tu navegador y ve a la URL donde se está ejecutando el frontend (e.g., `http://localhost:5173`).
2.  Ingresa las credenciales de un usuario existente en tu Keycloak.
3.  Haz clic en "Iniciar sesión".
4.  Si el login es exitoso, verás una alerta de confirmación y podrás verificar en las herramientas de desarrollo de tu navegador (pestaña `Application` -> `Local Storage`) que se han guardado las entradas `user` y `token`.