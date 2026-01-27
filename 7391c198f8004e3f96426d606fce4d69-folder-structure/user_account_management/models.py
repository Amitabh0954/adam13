from .extensions import db
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    last_login_at = db.Column(db.DateTime, nullable=True)
    current_login_at = db.Column(db.DateTime, nullable=True)
    login_count = db.Column(db.Integer, default=0, nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    invalid_login_attempts = db.Column(db.Integer, default=0, nullable=False)

class PasswordResetToken(db.Model):
    id = db.Column(db.Integer, primary key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reset_tokens', lazy=True))
    token = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)