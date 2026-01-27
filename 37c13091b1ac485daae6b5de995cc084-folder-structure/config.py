import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_temporary_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql+pymysql://user:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session settings
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = int(os.environ.get("PERMANENT_SESSION_LIFETIME", 1800))  # 30 minutes of inactivity

    # Application settings
    REMEMBER_COOKIE_DURATION = 3600  # 1 hour