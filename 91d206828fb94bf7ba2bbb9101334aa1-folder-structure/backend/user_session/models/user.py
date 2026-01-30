# Epic Title: User Account Management
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id: int, email: str):
        self.id = id
        self.email = email

    def get_id(self):
        return str(self.id)