from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

db = SQLAlchemy()

class Cart(db.Model):
    __tablename__ = 'carts'

    id = Column(Integer, Sequence('cart_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    session_id = Column(String(256), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship('CartItem', back_populates='cart')

    def __repr__(self) -> str:
        return f'<Cart {self.id}>'

class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = Column(Integer, Sequence('cart_item_id_seq'), primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    cart = relationship('Cart', back_populates='items')
    product = relationship('Product')

    def __repr__(self) -> str:
        return f'<CartItem {self.id}>'