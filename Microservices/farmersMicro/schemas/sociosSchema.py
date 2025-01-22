from pydantic import BaseModel

class SocioSchema(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: str
    direccion: str
    fecha_nacimiento: str
    estado: str

    class Config:
        orm_mode = True

