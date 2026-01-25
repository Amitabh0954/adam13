from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.email}>'