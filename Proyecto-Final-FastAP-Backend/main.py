from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt, JWTError

app = FastAPI()

# "Base de datos" temporal en memoria
users_db = []

class User(BaseModel):
    username: str
    password: str


# REGISTER
@app.post("/register")
def register(user: User):
    for u in users_db:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="El usuario ya existe")

    users_db.append({
        "username": user.username,
        "password": user.password
    })

    return {
        "message": "Usuario registrado correctamente",
        "username": user.username
    }


# LOGIN
@app.post("/login")
def login(data: User):
    for u in users_db:
        if u["username"] == data.username and u["password"] == data.password:
            return {
                "message": "Login exitoso",
                "username": data.username
            }

    raise HTTPException(status_code=401, detail="Credenciales inválidas")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)