from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    estado: str

    class Config:
        orm_mode = True