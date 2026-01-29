# Epic Title: User Account Management

from typing import Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    first_name: str = Column(String(255), nullable=True)
    last_name: str = Column(String(255), nullable=True)
    preferences: str = Column(String(255), nullable=True)  # JSON string for simplicity
    
    def __init__(self, user_id: int, first_name: str = "", last_name: str = "", preferences: str = "") -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.preferences = preferences