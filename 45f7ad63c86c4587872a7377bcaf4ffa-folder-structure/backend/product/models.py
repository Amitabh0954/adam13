# Epic Title: Product Catalog Management

from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)  # Assuming foreign key constraint
    attributes = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    
    category = relationship("Category", back_populates="products")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    products = relationship("Product", back_populates="category")
    children = relationship("Category", backref=backref('parent', remote_side=[id]))