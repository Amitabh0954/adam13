# Epic Title: User Account Management

from typing import Any
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_time: DateTime = Column(DateTime, default=datetime.datetime.utcnow)
    end_time: DateTime = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="sessions")

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id