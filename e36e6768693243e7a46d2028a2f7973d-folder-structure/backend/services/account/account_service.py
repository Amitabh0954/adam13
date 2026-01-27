# Epic Title: User Account Management

from backend.repositories.account.account_repository import AccountRepository
from backend.models.user import User
import re
from typing import Dict

class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

    def register_user(self, email: str, password: str) -> Dict[str, str]:
        if self.account_repository.get_user_by_email(email):
            return {'status': 'error', 'message': 'Email must be unique'}

        if not self.is_password_secure(password):
            return {'status': 'error', 'message': 'Password does not meet security criteria'}

        self.account_repository.create_user(email, password)
        return {'status': 'success', 'message': 'User registered successfully'}

    def is_password_secure(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True