from fastapi import APIRouter
from client import productos

router = APIRouter()

# Obtener productos
@router.get("/productos")
def obtener_productos():
    lista = []

    for producto in productos.find():
        producto["_id"] = str(producto["_id"])
        lista.append(producto)

    return lista


# Crear producto
@router.post("/productos")
def crear_producto(producto: dict):
    resultado = productos.insert_one(producto)
    producto["_id"] = str(resultado.inserted_id)

    return producto