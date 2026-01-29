# Epic Title: Shopping Cart Functionality

from typing import Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cart(Base):
    __tablename__ = 'carts'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=True)  # For logged-in users
    session_id: str = Column(String(255), nullable=True)  # For guest users
    
    user = relationship("User", back_populates="carts")
    items = relationship("CartItem", back_populates="cart")