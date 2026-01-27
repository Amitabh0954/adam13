# Epic Title: User Account Management

from backend.user_account_management.repositories.user_repository import UserRepository
from typing import Dict

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, email: str, hashed_password: str) -> Dict[str, str]:
        if self.user_repository.get_user_by_email(email):
            return {'status': 'error', 'message': 'Email already exists'}
        
        self.user_repository.create_user(email, hashed_password)
        return {'status': 'success', 'message': 'User registered successfully'}