from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite engine instance
SQLALCHEMY_DATABASE_URL = "postgresql://usuarios_k6ts_user:PexK3uCvlxJibK4mM5t3hXmx5VSzYtib@dpg-criuk1rv2p9s738p091g-a.oregon-postgres.render.com/usuarios_k6ts"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/usuarios"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
