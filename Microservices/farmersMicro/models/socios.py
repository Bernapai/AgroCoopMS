from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

class Socio(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: str
    direccion: str
    fecha_nacimiento: str
    estado: str

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
       