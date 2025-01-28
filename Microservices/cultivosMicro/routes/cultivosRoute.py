from fastapi import APIRouter
from config.database import cultivos_collection
from schemas.cultivosSchema import CultivoSchema
from bson import ObjectId

cultivoRoute = APIRouter()

@cultivoRoute.get("/cultivos")
def get_cultivos():
    cultivos = []
    for cultivo in cultivos_collection.find():
        cultivos.append({
            "id": str(cultivo["_id"]),
            "nombre": cultivo["nombre"],
            "descripcion": cultivo["descripcion"],
            "fecha_siembra": cultivo["fecha_siembra"],
            "fecha_estimada": cultivo["fecha_estimada"],
            "estado": cultivo["estado"]
        })
    return {"cultivos": cultivos}

@cultivoRoute.get("/cultivo/{id}")
def get_cultivo(id: str):
    cultivo = cultivos_collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(cultivo["_id"]),
        "nombre": cultivo["nombre"],
        "descripcion": cultivo["descripcion"],
        "fecha_siembra": cultivo["fecha_siembra"],
        "fecha_estimada": cultivo["fecha_estimada"],
        "estado": cultivo["estado"]
    }


@cultivoRoute.post("/cultivo")
def add_cultivo(cultivo: CultivoSchema):
    cultivo = dict(cultivo)
    cultivos_collection.insert_one(cultivo)
    return {"message": "Cultivo registrado exitosamente"}


@cultivoRoute.put("/cultivo/{id}")
def update_cultivo(id: str, cultivo: CultivoSchema):
    cultivo = dict(cultivo)
    cultivos_collection.update_one({"_id": ObjectId(id)}, {"$set": cultivo})
    return {"message": "Cultivo actualizado exitosamente"}

@cultivoRoute.delete("/cultivo/{id}")
def delete_cultivo(id: str):
    cultivos_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Cultivo eliminado exitosamente"}