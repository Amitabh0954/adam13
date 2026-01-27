# Epic Title: User Account Management

from backend.repositories.user_account.user_repository import UserRepository
import re

class RegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> dict:
        if self.user_repository.get_user_by_email(email):
            return {'status': 'error', 'message': 'Email already exists'}

        if not self._is_password_strong(password):
            return {'status': 'error', 'message': 'Password does not meet security criteria'}

        self.user_repository.create_user(email, password)
        return {'status': 'success', 'message': 'User registered successfully'}

    def _is_password_strong(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*]", password):
            return False
        return True