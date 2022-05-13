#https://fastapi.tiangolo.com/tutorial/sql-databases/
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQL Connection string to local DB (move to env)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

#session_maker stores the class for which instances will represent database sessions
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class from which models will inherit
Base = declarative_base()