# Epic Title: Shopping Cart Functionality

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    cart = Column(Text, nullable=True)  # Storing cart as JSON string

    @property
    def cart_dict(self):
        return json.loads(self.cart) if self.cart else {}

    @cart_dict.setter
    def cart_dict(self, value: dict):
        self.cart = json.dumps(value)