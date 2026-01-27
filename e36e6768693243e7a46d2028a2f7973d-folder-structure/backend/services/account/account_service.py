# Epic Title: User Account Management

from backend.repositories.account.account_repository import AccountRepository
from backend.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
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

        hashed_password = generate_password_hash(password)
        self.account_repository.create_user(email, hashed_password)
        return {'status': 'success', 'message': 'User registered successfully'}

    def login_user(self, email: str, password: str) -> Dict[str, str]:
        user = self.account_repository.get_user_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return {'status': 'error', 'message': 'Invalid email or password'}

        return {'status': 'success', 'message': 'User logged in successfully', 'user_id': user.id}

    def get_profile(self, user_id: int) -> Dict[str, str]:
        user = self.account_repository.get_user_by_id(user_id)
        if not user:
            return {}  # or raise an appropriate error

        return {
            'email': user.email,
            'name': user.name,
            'address': user.address
        }
    
    def update_profile(self, user_id: int, data: Dict[str, str]) -> Dict[str, str]:
        user = self.account_repository.get_user_by_id(user_id)
        if not user:
            return {'status': 'error', 'message': 'User not found'}

        if 'email' in data and data['email'] != user.email:
            if self.account_repository.get_user_by_email(data['email']):
                return {'status': 'error', 'message': 'Email must be unique'}
            user.email = data['email']

        if 'name' in data:
            user.name = data['name']

        if 'address' in data:
            user.address = data['address']

        self.account_repository.update_user(user)
        return {'status': 'success', 'message': 'Profile updated successfully'}

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