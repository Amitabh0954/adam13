# Epic Title: Product Catalog Management

from typing import Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False, unique=True)
    parent_id: int = Column(Integer, ForeignKey('categories.id'), nullable=True)
    
    products = relationship("Product", back_populates="category")
    subcategories = relationship("Category", back_populates="parent", remote_side=[id])
    
    parent = relationship("Category", back_populates="subcategories", remote_side=[id])
    
    def __init__(self, name: str, parent_id: int = None) -> None:
        self.name = name
        self.parent_id = parent_id