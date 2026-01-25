from backend.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    login_attempts = db.Column(db.Integer, default=0)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password