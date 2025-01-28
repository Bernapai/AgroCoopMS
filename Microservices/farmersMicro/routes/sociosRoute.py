from fastapi import APIRouter
from config.database import socios_collection
from schemas.sociosSchema import SocioSchema
from bson import ObjectId

socioRoute = APIRouter()

@socioRoute.get("/socios")
def get_socios():
    socios = []
    for socio in socios_collection.find():
        socios.append({
            "id": str(socio["_id"]),
            "nombre": socio["nombre"],
            "apellido": socio["apellido"],
            "dni": socio["dni"],
            "telefono": socio["telefono"],
            "direccion": socio["direccion"],
            "fecha_nacimiento": socio["fecha_nacimiento"],
            "estado": socio["estado"]
        })
    return {"socios": socios}

@socioRoute.get("/socio/{id}")
def get_socio(id: str):
    socio = socios_collection.find_one({"_id": ObjectId(id)})
    return {
        "id": str(socio["_id"]),
        "nombre": socio["nombre"],
        "apellido": socio["apellido"],
        "dni": socio["dni"],
        "telefono": socio["telefono"],
        "direccion": socio["direccion"],
        "fecha_nacimiento": socio["fecha_nacimiento"],
        "estado": socio["estado"]
    }
        

@socioRoute.post("/socio")
def add_socio(socio: SocioSchema):
    socio = dict(socio)
    socios_collection.insert_one(socio)
    return {"message": "Socio registrado exitosamente"}
    
@socioRoute.put("/socio/{id}")
def update_socio(id: str, socio: SocioSchema):
    socio = dict(socio)
    socios_collection.update_one({"_id": ObjectId(id)}, {"$set": socio})
    return {"message": "Socio actualizado exitosamente"}

@socioRoute.delete("/socio/{id}")
def delete_socio(id: str):
    socios_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Socio eliminado exitosamente"}