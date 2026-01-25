from backend.database import db
from sqlalchemy.dialects.mysql import JSON

class Profile(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    preferences = db.Column(JSON, nullable=True)