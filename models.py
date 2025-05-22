from sqlalchemy import Column, String, Date, ForeignKey
from database import Base
import uuid

class Profesion(Base):
    __tablename__ = 'profesiones'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100), nullable=False)

class TituloProfesional(Base):
    __tablename__ = 'titulos_profesionales'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    persona_id = Column(String(36), nullable=False)
    profesion_id = Column(String(36), ForeignKey('profesiones.id'), nullable=False)
    institucion = Column(String(100), nullable=False)
    fecha_obtencion = Column(Date, nullable=False)
    cedula = Column(String(20), nullable=False)
