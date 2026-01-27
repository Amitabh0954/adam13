from .extensions import db

def setup_database():
    db.create_all()

def send_email(subject: str, recipient: str, body: str):
    from flask_mail import Message
    from .extensions import mail

    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)

def pagination(query, page: int, per_page: int):
    return query.paginate(page, per_page, False)

def highlight(text: str, terms: list) -> str:
    for term in terms:
        text = text.replace(term, f"<b>{term}</b>")
    return text