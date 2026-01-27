from .models import db, User
from flask_mail import Message
from .extensions import mail

def setup_database():
    db.create_all()

def validate_password(password: str) -> bool:
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return False
    return True

def send_email(subject: str, recipients: list, text_body: str, html_body: str):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)