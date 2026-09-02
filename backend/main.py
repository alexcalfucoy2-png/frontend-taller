from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ======= API =======
# Creamos nuestra API usando FastAPI
app = FastAPI()

#Frontend: parte que ve y usa el usuario
# Permite que el frontend se conecte con la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lista donde guardamos los usuarios
usuarios = []

# GET: obtener usuarios
@app.get("/usuarios")
def obtener_usuarios():
    return usuarios

# POST: crear usuario
@app.post("/usuarios")
def crear_usuario(usuario: dict):
    usuarios.append(usuario)
    return usuario

# DELETE: eliminar usuario
@app.delete("/usuarios/{indice}")
def eliminar_usuario(indice: int):
    usuarios.pop(indice)
    return {"mensaje": "Usuario eliminado"}