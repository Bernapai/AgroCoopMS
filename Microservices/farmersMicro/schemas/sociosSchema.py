from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime
from typing import Literal

class SocioSchema(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: str
    direccion: str
    fecha_nacimiento: datetime
    estado: Literal['activo', 'inactivo']

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
       

