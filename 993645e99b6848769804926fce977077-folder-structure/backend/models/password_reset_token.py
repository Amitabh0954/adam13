from backend.database import db
import uuid
from datetime import datetime, timedelta

class PasswordResetToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    expiration = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow() + timedelta(hours=24))