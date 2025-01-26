from fastapi import APIRouter
from config.database import ventas_collection
from schemas.ventasSchema import VentasSchema
from bson import ObjectId

ventasRoute = APIRouter()

@ventasRoute.get("/ventas")
def get_ventas():
    ventas = []
    for venta in ventas_collection.find():
        ventas.append({
            "id": str(venta["_id"]),
            "name_producto": venta["name_producto"],
            "cantidad": venta["cantidad"],
            "total": venta["total"],
            "fecha": venta["fecha"],
            "estado": venta["estado"]
        })
    return {"ventas": ventas}

@ventasRoute.get("/venta/{id}")
def get_venta(id: str):
    venta = ventas_collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(venta["_id"]),
        "name_producto": venta["name_producto"],
        "cantidad": venta["cantidad"],
        "total": venta["total"],
        "fecha": venta["fecha"],
        "estado": venta["estado"]
    }

@ventasRoute.post("/venta")
def add_venta(venta: VentasSchema):
    venta = dict(venta)
    ventas_collection.insert_one(venta)
    return {"message": "Venta registrada exitosamente"}

@ventasRoute.put("/venta/{id}")
def update_venta(id: str, venta: VentasSchema):
    venta = dict(venta)
    ventas_collection.update_one({"_id": ObjectId(id)}, {"$set": venta})
    return {"message": "Venta actualizada exitosamente"}

@ventasRoute.delete("/venta/{id}")
def delete_venta(id: str):
    ventas_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Venta eliminada exit

