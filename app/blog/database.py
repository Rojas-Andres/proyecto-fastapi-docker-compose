from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
from dotenv import load_dotenv
import os 
import sys 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv("../.env")
SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5435/postgres'

engine = create_engine(SQLALCHEMY_DATABASE_URL)#, #connect_args={"check_same_thread":False})

SessionLocal = scoped_session(sessionmaker(bind=engine,autocommit=False,autoflush=False))
Base = declarative_base()

Base.query = SessionLocal.query_property()


#Conexion
def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()
