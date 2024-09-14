from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Create a sqlite engine instance
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
LOCALHOST_URL = os.getenv('LOCALHOST_URL')

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
