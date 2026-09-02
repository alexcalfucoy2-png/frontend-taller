from pymongo import MongoClient

# Conexión con MongoDB
client = MongoClient("mongodb+srv://AlexCalfucoy:48411088@cluster0.ljypavq.mongodb.net/?appName=Cluster0")

# Base de datos
db = client["taller"]

# Colecciones
usuarios = db["usuarios"]
productos = db["productos"]