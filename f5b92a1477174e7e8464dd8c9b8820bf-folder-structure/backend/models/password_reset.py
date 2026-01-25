from backend.database import db
from datetime import datetime

class PasswordReset(db.Model):
    token = db.Column(db.String(120), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expiry = db.Column(db.DateTime, nullable=False)
    user = db.relationship('User')