from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from user import router as user_router
from productos import router as productos_router

# Crear API
app = FastAPI()

# Permitir frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Rutas
app.include_router(user_router)
app.include_router(productos_router)



# API = permite la comunicación entre el frontend y el backend.
# Frontend = parte de la aplicación que ve el usuario (HTML, CSS y JS).
# Endpoint = URL específica del backend para realizar una acción.
# Backend = trabaja detrás de la página
# JSON = formato usado para enviar y recibir datos.
# Fetch = función que permite hacer pedidos HTTP. conecta JavaScript con la API

# GET = obtener datos
# POST = crear datos
# MongoDB = guarda los datos

#FastAPI = framework de Python que crea y maneja la API, procesa el pedido
# await = espera la respuesta de la API
# async = permite usar await dentro de una función
# Vanilla JS = JavaScript sin frameworks ni librerías.
# DOM = representación del HTML que JavaScript puede leer y modificar.
# Promesa = resultado que llegará más adelante y se puede esperar con await.
# CORS = permite que el frontend se comunique con el backend.
# Uvicorn = ejecuta el servidor FastAPI
