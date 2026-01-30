# Epic Title: User Account Management
from repositories.user_management.user_repository import UserRepository
from backend.models.user import User
import bcrypt

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate_user(self, email: str, password: str) -> User:
        user_data = self.user_repository.get_user_by_email(email)
        if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data['password'].encode('utf-8')):
            return User(user_data['id'], user_data['email'])
        return None