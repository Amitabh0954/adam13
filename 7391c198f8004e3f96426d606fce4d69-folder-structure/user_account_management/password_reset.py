from datetime import datetime, timedelta
from flask import url_for, current_app
from itsdangerous import URLSafeTimedSerializer
from .extensions import mail, db
from .models import User, PasswordResetToken
from flask_mail import Message

def get_password_reset_token(user: User) -> str:
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = serializer.dumps(user.email, salt='password-reset-salt')
    expiration_time = datetime.utcnow() + timedelta(hours=24)
    reset_token = PasswordResetToken(user_id=user.id, token=token, created_at=expiration_time)
    db.session.add(reset_token)
    db.session.commit()
    return token

def validate_password_reset_token(token: str) -> User:
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=86400)
    except Exception:
        return None
    user = User.query.filter_by(email=email).first()
    if user:
        reset_token = PasswordResetToken.query.filter_by(token=token, user_id=user.id).first()
        if reset_token:
            db.session.delete(reset_token)
            db.session.commit()
            return user
    return None

def send_password_reset_email(to_email: str, token: str):
    reset_link = url_for('user.reset_password', token=token, _external=True)
    msg = Message(subject="Password Reset Request",
                  recipients=[to_email],
                  body=f"Please click the following link to reset your password: {reset_link}")
    mail.send(msg)