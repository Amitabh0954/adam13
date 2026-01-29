# Epic Title: Product Catalog Management

from typing import Any
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False, unique=True)
    price: float = Column(Float, nullable=False)
    description: str = Column(String(255), nullable=False)
    category_id: int = Column(Integer, ForeignKey('categories.id'), nullable=False)
    
    category = relationship("Category", back_populates="products")
    
    def __init__(self, name: str, price: float, description: str, category_id: int) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id