from backend.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    carts = db.relationship('Cart', back_populates='user', cascade='all, delete-orphan')