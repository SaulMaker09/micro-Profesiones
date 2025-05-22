from pydantic import BaseModel
from datetime import date

class ProfesionSchema(BaseModel):
    id: str | None = None
    nombre: str

    class Config:
        orm_mode = True

class TituloSchema(BaseModel):
    id: str | None = None
    persona_id: str
    profesion_id: str
    institucion: str
    fecha_obtencion: date
    cedula: str

    class Config:
        orm_mode = True
