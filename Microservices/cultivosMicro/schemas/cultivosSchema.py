from pydantic import BaseModel
from datetime import datetime
from typing import Literal
from bson import ObjectId

class CultivoSchema(BaseModel):
    nombre: str
    descripcion: str
    fecha_siembra: datetime
    fecha_estimada: datetime
    estado:  Literal['germinando', 'en crecimiento', 'maduro', 'cosechado']

    class Config:
        orm_mode = True
        # MongoDB utiliza ObjectId como el tipo de _id
        json_encoders = {
            ObjectId: str  # Para que al serializar convierta ObjectId a str
        }