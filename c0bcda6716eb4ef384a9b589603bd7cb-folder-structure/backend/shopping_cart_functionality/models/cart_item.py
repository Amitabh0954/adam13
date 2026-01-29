# Epic Title: Shopping Cart Functionality

from typing import Any
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CartItem(Base):
    __tablename__ = 'cart_items'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    cart_id: int = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id: int = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity: int = Column(Integer, nullable=False, default=1)
    
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")