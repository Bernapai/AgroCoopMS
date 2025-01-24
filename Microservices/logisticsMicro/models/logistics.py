from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class LogisticSchema(BaseModel):
    nombre: str
    descripcion: str
    fecha_entrega: datetime
    estado:  Literal['en camino', 'entregado']

    class Config:
        orm_mode = True
      