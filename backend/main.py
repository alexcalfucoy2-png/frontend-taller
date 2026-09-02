from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargamos las variables
load_dotenv()

# Creamos la API
app = FastAPI()

# Permitimos conectar el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== MONGODB =====

# Conectamos con MongoDB
cliente = MongoClient(os.getenv("MONGO_URL"))

# Base de datos
db = cliente["mi_base"]

# Colección de usuarios
usuarios = db["usuarios"]


# ===== RUTAS =====

# GET: obtener usuarios
@app.get("/usuarios")
def obtener_usuarios():

    lista = []

    for usuario in usuarios.find():
        usuario["_id"] = str(usuario["_id"])
        lista.append(usuario)

    return lista


# POST: crear usuario
@app.post("/usuarios")
def crear_usuario(usuario: dict):

    resultado = usuarios.insert_one(usuario)

    usuario["_id"] = str(resultado.inserted_id)

    return usuario


# DELETE: eliminar usuario
@app.delete("/usuarios/{id}")
def eliminar_usuario(id: str):

    from bson import ObjectId

    usuarios.delete_one({
        "_id": ObjectId(id)
    })

    return {"mensaje": "Usuario eliminado"}