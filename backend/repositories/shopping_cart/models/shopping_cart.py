from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
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
    total_price = Column(Float, default=0.0)

    items = relationship('ShoppingCartItem', back_populates='cart')

    def update_total_price(self):
        self.total_price = sum(item.price * item.quantity for item in self.items)

#### 2. Create repositories for managing the removal of cart items