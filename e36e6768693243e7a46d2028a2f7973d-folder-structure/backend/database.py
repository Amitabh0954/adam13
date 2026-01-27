# Epic Title: Product Catalog Management

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import Pagination

DATABASE_URI = 'mysql+pymysql://user:password@localhost/db_name'

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()