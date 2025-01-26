from pydantic import BaseModel

class Venta(BaseModel):
    name_producto: str
    cantidad: int
    total: float
    fecha: str

    class Config:
        orm_mode = True