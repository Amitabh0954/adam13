from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean, Sequence

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(Float, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f'<Product {self.name}>'