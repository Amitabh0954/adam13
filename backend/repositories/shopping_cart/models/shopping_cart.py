from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True)
    session_id = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship('ShoppingCartItem', back_populates='cart')