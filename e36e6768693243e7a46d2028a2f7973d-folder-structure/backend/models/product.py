# Epic Title: Product Catalog Management

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='products')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category_id': self.category_id,
            'category_name': self.category.name
        }

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    parent = relationship('Category', remote_side=[id], back_populates='children')
    children = relationship('Category', remote_side=[parent_id], back_populates='parent')

    products = relationship('Product', back_populates='category')