# Epic Title: Product Catalog Management

from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    category = Column(String(200), nullable=False)
    attributes = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)