from sqlmodel import SQLModel, create_engine, Session
from sqlmodel import select
from app.models import Patient
import os

DB_URL = os.environ.get('DATABASE_URL', 'sqlite:///./prototype-backend.db')
engine = create_engine(DB_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
