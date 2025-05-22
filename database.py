from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = 'mysql://root:wJlmkFlCpWWSuJCbiJKfjcmLKmPtCEHm@yamabiko.proxy.rlwy.net:51332/railway'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
