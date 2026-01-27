from flask_mail import Message
from user_account_management.extensions import mail

def send_email(subject: str, recipients: list, text_body: str, html_body: str):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)