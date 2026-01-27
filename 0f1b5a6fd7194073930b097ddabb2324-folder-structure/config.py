import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_temporary_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql+pymysql://user:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security and session management settings
    REMEMBER_COOKIE_DURATION = 3600  # 1 hour
    PERMANENT_SESSION_LIFETIME = 1800  # 30 minutes of inactivity