# Inline comment referencing the Epic Title
# Epic Title: Shopping Cart Functionality

from itsdangerous import URLSafeTimedSerializer
from .extensions import db

def generate_token(email: str):
    serializer = URLSafeTimedSerializer(secret_key="SECRET_KEY")
    return serializer.dumps(email, salt="email-confirm-salt")

def confirm_token(token: str, expiration=86400):  # Token expiration set to 24 hours (86400 seconds)
    serializer = URLSafeTimedSerializer(secret_key="SECRET_KEY")
    try:
        email = serializer.loads(token, salt="email-confirm-salt", max_age=expiration)
    except:
        return False
    return email

def send_email(subject: str, recipient: str, body: str):
    from flask_mail import Message
    from .extensions import mail

    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)

def setup_database():
    db.create_all()