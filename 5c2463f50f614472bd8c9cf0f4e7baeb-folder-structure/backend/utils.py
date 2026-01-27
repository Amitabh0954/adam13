from .extensions import db

def setup_database():
    db.create_all()

def send_email(subject: str, recipient: str, body: str):
    from flask_mail import Message
    from .extensions import mail

    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)