from sqlalchemy import Column, Integer, String, Float, DateTime, UniqueConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (UniqueConstraint('name', name='unique_product_name'),)

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(255), nullable=True)
    attributes = Column(String(255), nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#### 2. Create a repository for managing product searches