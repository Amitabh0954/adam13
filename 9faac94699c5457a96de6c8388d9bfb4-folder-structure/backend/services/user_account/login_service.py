# Epic Title: User Account Management

from backend.repositories.user_account.user_repository import UserRepository
from werkzeug.security import check_password_hash

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {'status': 'error', 'message': 'Invalid email or password'}

        if not check_password_hash(user.password, password):
            return {'status': 'error', 'message': 'Invalid email or password'}

        return {'status': 'success', 'user': user}