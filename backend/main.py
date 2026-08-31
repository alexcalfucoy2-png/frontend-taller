from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

usuarios = []


@app.get("/usuarios")
def obtener_usuarios():
    return usuarios


@app.post("/usuarios")
def crear_usuario(usuario: dict):
    usuarios.append(usuario)
    return usuario