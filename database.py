from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://sanjay:uNWClHbhbDmgu68j1oouLancZC81ocdR@dpg-cur1t0t2ng1s73cl0pkg-a.oregon-postgres.render.com/celeberationex_data"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
