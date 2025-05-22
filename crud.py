from sqlalchemy.orm import Session
import models, schemas

def crear_profesion(db: Session, profesion: schemas.ProfesionSchema):
    nueva = models.Profesion(nombre=profesion.nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def crear_titulo(db: Session, titulo: schemas.TituloSchema):
    nuevo = models.TituloProfesional(**titulo.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
