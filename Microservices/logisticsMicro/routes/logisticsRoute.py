from fastapi import APIRouter
from config.database import logistics_collection
from schemas.logisticsSchema import LogisticSchema
from bson import ObjectId


logisticsRoute = APIRouter()

@logisticsRoute.get("/logistics")
def get_logistics():
    logistics = []
    for logistic in logistics_collection.find():
        logistics.append({
            "id": str(logistic["_id"]),
            "nombre": logistic["nombre"],
            "descripcion": logistic["descripcion"],
            "fecha_inicio": logistic["fecha_inicio"],
            "fecha_fin": logistic["fecha_fin"],
            "estado": logistic["estado"]
        })
    return {"logistics": logistics}

@logisticsRoute.get("/logistic/{id}")
def get_logistic(id: str):
    logistic = logistics_collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(logistic["_id"]),
        "nombre": logistic["nombre"],
        "descripcion": logistic["descripcion"],
        "fecha_inicio": logistic["fecha_inicio"],
        "fecha_fin": logistic["fecha_fin"],
        "estado": logistic["estado"]
   }

@logisticsRoute.post("/logistic")
def add_logistic(logistic: LogisticSchema):
    logistic = dict(logistic)
    logistics_collection.insert_one(logistic)
    return {"message": "Logistic registrado exitosamente"}

@logisticsRoute.put("/logistic/{id}")
def update_logistic(id: str, logistic: LogisticSchema):
    logistic = dict(logistic)
    logistics_collection.update_one({"_id": ObjectId(id)}, {"$set": logistic})
    return {"message": "Logistic actualizado exitosamente"}

@logisticsRoute.delete("/logistic/{id}")
def delete_logistic(id: str):
    logistics_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Logistic eliminado exitosamente"}