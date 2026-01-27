# Epic Title: User Account Management

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    preferences = Column(Text, nullable=True)  # New preferences column
    saved_cart = Column(Text, nullable=True)  # New saved cart column