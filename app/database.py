from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base

# TODO :- Import models

DATABASE_URL = "postgresql+psycopg2://postgres:justdev@localhost:5432/notesDB"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()