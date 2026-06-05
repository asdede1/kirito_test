from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette.responses import Response
import asyncio
from database import engine, SessionLocal, Base, Pas, Pass, MainSchema,  Passchema
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене тут должен быть конкретный адрес, для тестов — "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/all_pass", response_model=list[Passchema])
def get_all_pass(db: Session = Depends(get_db)):
    all_pass = db.query(Pass).all()
    return all_pass
@app.get("/pas/{pas_id}", response_model=list[Passchema])
def get_pas(pas_id: int, db: Session = Depends(get_db)):
    res = db.query(Pass).filter(Pass.main_id == pas_id).all()
    return res
@app.post("/pas", response_model=Passchema)
def create_pas(pas: Passchema, db: Session = Depends(get_db)):
    db_passenger = Pass(
        main_id=pas.main_id,
        name=pas.name,
        ticket=pas.ticket,
        place=pas.place,
    )
    db.add(db_passenger)  # Кладем в сессию
    db.commit()  # Сохраняем в БД
    db.refresh(db_passenger)  # Обновляем объект, чтобы получить его ID из базы
    return db_passenger