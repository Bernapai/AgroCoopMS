from fastapi import APIRouter
from config.database import productos_collection
from schemas.productoSchema import ProductoSchema
from bson import ObjectId

productoRoute = APIRouter()

@productoRoute.get("/productos")
def get_productos():
    productos = []
    for producto in productos_collection.find():
        productos.append({
            "id": str(producto["_id"]),
            "nombre": producto["nombre"],
            "descripcion": producto["descripcion"],
            "precio": producto["precio"],
            "stock": producto["stock"],
            "estado":producto["estado"]
        })
    return {"productos": productos}

@productoRoute.get("/producto/{id}")
def get_producto(id: str):
    producto = productos_collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(producto["_id"]),
        "nombre": producto["nombre"],
        "descripcion": producto["descripcion"],
        "precio": producto["precio"],
        "stock": producto["stock"],
        "estado":producto["estado"]
    }

@productoRoute.post("/producto")
def add_producto(producto: ProductoSchema):
    producto = dict(producto)
    productos_collection.insert_one(producto)
    return {"message": "Producto registrado exitosamente"}

@productoRoute.put("/producto/{id}")
def update_producto(id: str, producto: ProductoSchema):
    producto = dict(producto)
    productos_collection.update_one({"_id": ObjectId(id)}, {"$set": producto})
    return {"message": "Producto actualizado exitosamente"}

@productoRoute.delete("/producto/{id}")
def delete_producto(id: str):
    productos_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Producto eliminado exitosamente"}