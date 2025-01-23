from pydantic import BaseModel

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