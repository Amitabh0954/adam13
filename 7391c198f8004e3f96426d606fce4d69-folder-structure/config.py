import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_temporary_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql+pymysql://user:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False