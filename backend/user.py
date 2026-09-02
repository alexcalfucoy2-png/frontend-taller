from fastapi import APIRouter
from client import usuarios
from bson import ObjectId

router = APIRouter()

# Obtener usuarios
@router.get("/usuarios")
def obtener_usuarios():
    lista = []

    for usuario in usuarios.find():
        usuario["_id"] = str(usuario["_id"])
        lista.append(usuario)

    return lista

# Crear usuario
@router.post("/usuarios")
def crear_usuario(usuario: dict):
    resultado = usuarios.insert_one(usuario)
    usuario["_id"] = str(resultado.inserted_id)

    return usuario

# Eliminar usuario
@router.delete("/usuarios/{id}")
def eliminar_usuario(id: str):
    usuarios.delete_one({"_id": ObjectId(id)})
    return {"mensaje": "Usuario eliminado correctamente"}