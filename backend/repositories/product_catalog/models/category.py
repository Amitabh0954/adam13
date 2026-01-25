from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    parent = relationship('Category', remote_side=[id], backref='children')