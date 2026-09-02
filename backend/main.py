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