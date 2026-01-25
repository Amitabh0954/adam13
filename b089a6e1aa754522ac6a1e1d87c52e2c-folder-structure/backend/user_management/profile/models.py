from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, Boolean, DateTime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    address = Column(String(255), nullable=True)
    city = Column(String(50), nullable=True)
    country = Column(String(50), nullable=True)
    phone_number = Column(String(20), nullable=True)
    
    # Track login attempts and lock time
    failed_login_attempts = Column(Integer, default=0, nullable=False)
    account_locked_until = Column(DateTime, nullable=True)
    
    def __repr__(self) -> str:
        return f'<User {self.email}>'