# Epic Title: User Account Management

from backend.user_account_management.repositories.user_repository import UserRepository
from backend.user_account_management.models.user import User
from typing import Dict
import re

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def validate_email(self, email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def validate_password(self, password: str) -> bool:
        return len(password) >= 8 and bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password)) and bool(re.search(r'[0-9]', password))

    def send_confirmation_email(self, email: str) -> None:
        # Placeholder implementation
        print(f"Confirmation email sent to {email}")

    def create_user(self, email: str, hashed_password: str) -> Dict[str, str]:
        if not self.validate_email(email):
            return {'status': 'error', 'message': 'Invalid email format'}

        if not self.validate_password(hashed_password):
            return {'status': 'error', 'message': 'Password does not meet complexity requirements'}

        if self.user_repository.get_user_by_email(email):
            return {'status': 'error', 'message': 'Email already exists'}

        self.user_repository.create_user(email, hashed_password)
        self.send_confirmation_email(email)
        return {'status': 'success', 'message': 'User registered successfully'}

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)