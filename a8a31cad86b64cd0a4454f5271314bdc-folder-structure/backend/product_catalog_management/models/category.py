# Epic Title: Product Catalog Management

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    children = relationship("Category")