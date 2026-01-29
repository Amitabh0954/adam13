# Epic Title: User Account Management

from typing import Any
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    email: str = Column(String(255), nullable=False, unique=True)
    password: str = Column(String(255), nullable=False)
    
    __table_args__ = (
        UniqueConstraint('email', name='uq_email'),
    )
    
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password