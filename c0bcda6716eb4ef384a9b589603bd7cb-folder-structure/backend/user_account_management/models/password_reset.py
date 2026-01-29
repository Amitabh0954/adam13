# Epic Title: User Account Management

from typing import Any
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class PasswordReset(Base):
    __tablename__ = 'password_resets'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    token: str = Column(String(255), nullable=False, unique=True)
    expires_at: DateTime = Column(DateTime, default=lambda: datetime.datetime.utcnow() + datetime.timedelta(hours=24))

    def __init__(self, user_id: int, token: str) -> None:
        self.user_id = user_id
        self.token = token