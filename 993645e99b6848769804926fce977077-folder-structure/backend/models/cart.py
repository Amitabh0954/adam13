from backend.database import db
from sqlalchemy.dialects.mysql import JSON

class Cart(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    items = db.Column(JSON, nullable=False)