from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class CultivoSchema(BaseModel):
    nombre: str
    descripcion: str
    fecha_siembra: datetime
    fecha_estimada: datetime
    estado:  Literal['germinando', 'en crecimiento', 'maduro', 'cosechado']

    class Config:
        orm_mode = True
        