from datetime import date
from sqlalchemy import create_engine, String, Date, select, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session, relationship
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
load_dotenv()
URL = os.getenv("URL")
engine = create_engine(URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass


class Pas(Base):
    __tablename__ = 'main'
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[date] = mapped_column(Date)
    passa: Mapped[list['Pass']] = relationship(back_populates='date_r')


class Pass(Base):
    __tablename__ = 'pas_cl'
    main_id: Mapped[int] = mapped_column(ForeignKey("main.id"))
    cl_id: Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str]
    ticket: Mapped[int]
    place: Mapped[int]
    date_r: Mapped['Pas'] = relationship(back_populates='passa')


class Passchema(BaseModel):
    main_id: int
    name: str = Field(min_length=1, max_length=25)
    ticket: int
    place: int = Field(gt = 1, lt = 50)
class Pascreat(Passchema):
    cl_id: int

    class Config:
        from_attributes = True
class MainSchema(BaseModel):
    id: int
    data: date
    passa: list["Passchema"]

    class Config:
        from_attributes = True






