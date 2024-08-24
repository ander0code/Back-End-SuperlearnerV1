#conexion a data base
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

import os

from dotenv import load_dotenv

load_dotenv()

database_conection = os.getenv("DATABASECONNECTION")

engine = create_engine(f'mysql+pymysql://{database_conection}')

conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()