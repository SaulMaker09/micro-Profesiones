from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/profesiones/")
def crear_profesion(p: schemas.ProfesionSchema, db: Session = Depends(get_db)):
    return crud.crear_profesion(db, p)

@app.post("/titulos/")
def crear_titulo(t: schemas.TituloSchema, db: Session = Depends(get_db)):
    return crud.crear_titulo(db, t)
