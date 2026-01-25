from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, Boolean, DateTime, ForeignKey
import datetime
import uuid

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Track login attempts and lock time
    failed_login_attempts = Column(Integer, default=0, nullable=False)
    account_locked_until = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f'<User {self.email}>'

class PasswordResetToken(db.Model):
    __tablename__ = 'password_reset_tokens'

    id = Column(Integer, Sequence('token_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'<PasswordResetToken {self.token} for user {self.user_id}>'