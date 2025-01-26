from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/')

# Selecciona la base de datos
db = conn["Productos"]  # Reemplaza con el nombre de tu base de datos

# Selección de colección (equivalente a una tabla en bases relacionales)
productos_collection = db["Productos"]