from sqlalchemy.orm import Session
import models, schemas

# ----------------------
# PROFESIONES
# ----------------------

def crear_profesion(db: Session, profesion: schemas.ProfesionSchema):
    nueva = models.Profesion(
        nombre_profesion=profesion.nombre_profesion,
        descripcion=profesion.descripcion
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_profesion(db: Session, profesion_id: int):
    return db.query(models.Profesion).filter(models.Profesion.id_profesion == profesion_id).first()

def obtener_profesiones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profesion).offset(skip).limit(limit).all()

def actualizar_profesion(db: Session, profesion_id: int, profesion_data: schemas.ProfesionSchema):
    profesion = db.query(models.Profesion).filter(models.Profesion.id_profesion == profesion_id).first()
    if profesion:
        profesion.nombre_profesion = profesion_data.nombre_profesion
        profesion.descripcion = profesion_data.descripcion
        db.commit()
        db.refresh(profesion)
    return profesion

def eliminar_profesion(db: Session, profesion_id: int):
    profesion = db.query(models.Profesion).filter(models.Profesion.id_profesion == profesion_id).first()
    if profesion:
        db.delete(profesion)
        db.commit()
    return profesion

# ----------------------
# TITULOS PROFESIONALES
# ----------------------

def crear_titulo(db: Session, titulo: schemas.TituloSchema):
    nuevo = models.TituloProfesional(**titulo.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_titulo(db: Session, titulo_id: int):
    return db.query(models.TituloProfesional).filter(models.TituloProfesional.id_titulo == titulo_id).first()

def obtener_titulos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TituloProfesional).offset(skip).limit(limit).all()

def obtener_titulos_por_persona(db: Session, persona_id: str):
    return db.query(models.TituloProfesional).filter(models.TituloProfesional.persona_id == persona_id).all()

def actualizar_titulo(db: Session, titulo_id: int, titulo_data: schemas.TituloSchema):
    titulo = db.query(models.TituloProfesional).filter(models.TituloProfesional.id_titulo == titulo_id).first()
    if titulo:
        for key, value in titulo_data.dict().items():
            setattr(titulo, key, value)
        db.commit()
        db.refresh(titulo)
    return titulo

def eliminar_titulo(db: Session, titulo_id: int):
    titulo = db.query(models.TituloProfesional).filter(models.TituloProfesional.id_titulo == titulo_id).first()
    if titulo:
        db.delete(titulo)
        db.commit()
    return titulo
