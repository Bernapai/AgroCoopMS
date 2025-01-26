from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime
from typing import Literal

class ProductoSchema(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    estado: Literal['activo', 'inactivo']

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
      