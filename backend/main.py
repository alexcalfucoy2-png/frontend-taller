from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Backend y API: parte que funciona detrás de la página.
# Recibe y devuelve los datos del frontend.
# Está hecha con Python y FastAPI.

#Frontend: parte que ve y usa el usuario.
#Está hecho con HTML, CSS y JavaScript.
#JavaScript se comunica con la API para obtener,
#crear y eliminar usuarios.

# ===== API ======
# Creamos nuestra API usando FastAPI
app = FastAPI()

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