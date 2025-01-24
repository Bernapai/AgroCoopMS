from pydantic import BaseModel
from datetime import datetime
from typing import Literal
from bson import ObjectId


class LogisticSchema(BaseModel):
    nombre: str
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: datetime
    estado:  Literal['en camino', 'en espera', 'entregado']

    class Config:
        orm_mode = True
        # MongoDB utiliza ObjectId como el tipo de _id
        json_encoders = {
            ObjectId: str  # Para que al serializar convierta ObjectId a str
        }