# Epic Title: User Account Management

import re
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, id: int, email: str, password: str):
        self.id = id
        self.email = email
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def validate_email(email: str) -> bool:
        return re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email) is not None

    @staticmethod
    def validate_password(password: str) -> bool:
        return (
            len(password) >= 8
            and re.search(r'\d', password)
            and re.search(r'[A-Z]', password)
            and re.search(r'[a-z]', password)
            and re.search(r'[\W_]', password)
        )

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)