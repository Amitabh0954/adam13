# Epic Title: Shopping Cart Functionality

from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    items = relationship("CartItem", back_populates="cart")

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'items': [
                {'product_id': item.product_id, 'quantity': item.quantity} for item in self.items
            ]
        }

class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    preferences = Column(Text, nullable=True)
    saved_cart = Column(Text, nullable=True)  # New field for storing saved cart JSON

    def load_cart(self) -> dict:
        return json.loads(self.saved_cart)