from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
load_dotenv()
import os
DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)
session_local = sessionmaker(bind=engine, autoflush=False) 

Base = declarative_base()
