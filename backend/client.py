from pymongo import MongoClient

# Conexión con MongoDB
client = MongoClient("mongodb+srv://AlexCalfucoy:48411088@cluster0.ljypavq.mongodb.net/?appName=Cluster0")

# Base de datos
db = client["taller"]

# Colecciones
usuarios = db["usuarios"]
productos = db["productos"]

# Frontend = lo que ve el usuario
# Backend = trabaja detrás de la página
# API = comunica frontend y backend
# GET = obtener datos
# POST = crear datos
# DELETE = eliminar datos
# MongoDB = guarda los datos
# JSON = formato para enviar datos
# Fetch = conecta JavaScript con la API
# Uvicorn = ejecuta el servidor FastAPI
# Git = guarda versiones del proyecto
# GitHub = guarda el proyecto online