from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime
from typing import Literal

class VentasSchema(BaseModel):
    name_producto: str
    cantidad: int
    total: float
    fecha: datetime
    estado: Literal['pagado', 'pendiente']

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }