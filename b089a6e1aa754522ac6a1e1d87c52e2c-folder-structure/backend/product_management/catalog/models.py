from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Sequence
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, Sequence('category_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    parent = relationship('Category', remote_side=[id], backref='subcategories')

    def __repr__(self) -> str:
        return f'<Category {self.name}>'

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', backref='products')

    is_deleted = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'<Product {self.name}>'