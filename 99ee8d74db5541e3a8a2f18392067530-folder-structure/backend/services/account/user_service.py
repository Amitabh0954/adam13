# Epic Title: User Account Management

from backend.repositories.user_repository.user_repository import UserRepository
import re
from typing import Dict

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.failed_login_attempts = {}
        
    def register_user(self, email: str, password: str) -> Dict[str, str]:
        if not self.is_email_unique(email):
            return {'status': 'error', 'message': 'Email already exists'}
        
        if not self.is_password_secure(password):
            return {'status': 'error', 'message': 'Password does not meet security criteria'}

        self.user_repository.create_user(email, password)
        return {'status': 'success', 'message': 'User registered successfully'}

    def login_user(self, email: str, password: str) -> Dict[str, str]:
        user = self.user_repository.get_user_by_email_and_password(email, password)
        if not user:
            self.track_failed_login(email)
            return {'status': 'error', 'message': 'Invalid email or password'}

        self.reset_failed_login_attempts(email)
        return {'status': 'success', 'user_id': user.id}

    def track_failed_login(self, email: str):
        if email not in self.failed_login_attempts:
            self.failed_login_attempts[email] = 0
        self.failed_login_attempts[email] += 1
    
    def reset_failed_login_attempts(self, email: str):
        if email in self.failed_login_attempts:
            self.failed_login_attempts[email] = 0

    def is_email_unique(self, email: str) -> bool:
        return self.user_repository.get_user_by_email(email) is None

    def is_password_secure(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

    def update_user_profile(self, user_id: int, data: Dict[str, str]) -> Dict[str, str]:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return {'status': 'error', 'message': 'User not found'}

        user.name = data.get('name', user.name)
        user.address = data.get('address', user.address)
        self.user_repository.update_user(user)
        return {'status': 'success', 'message': 'Profile updated successfully'}

    def get_user_profile(self, user_id: int) -> Dict[str, str]:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return None
        return {"name": user.name, "email": user.email, "address": user.address}