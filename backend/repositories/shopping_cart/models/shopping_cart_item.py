from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShoppingCartItem(Base):
    __tablename__ = 'shopping_cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('shopping_carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False)

    cart = relationship('ShoppingCart', back_populates='items')
    product = relationship('Product')

#### 2. Create repositories for managing shopping carts and cart items