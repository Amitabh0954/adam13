# Epic Title: User Account Management

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class PasswordReset(Base):
    __tablename__ = 'password_resets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String(255), unique=True, nullable=False)
    created_at = Column(String, default=datetime.datetime.utcnow)

    user = relationship('User')