# Epic Title: User Account Management
from repositories.user_session_repository import UserSessionRepository
from flask_login import UserMixin

class UserSessionService:
    def __init__(self):
        self.user_session_repository = UserSessionRepository()

    def authenticate_user(self, email: str, password: str) -> UserMixin | None:
        user = self.user_session_repository.get_user_by_email(email)
        if user and self.user_session_repository.verify_password(user['password'], password):
            return User(user['id'], user['email'])
        return None

class User(UserMixin):
    def __init__(self, id: int, email: str):
        self.id = id
        self.email = email

    def get_id(self):
        return self.id