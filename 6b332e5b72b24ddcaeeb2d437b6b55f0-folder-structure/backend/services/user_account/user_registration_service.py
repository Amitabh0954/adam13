# Epic Title: User Registration

from backend.repositories.user_repository import UserRepository
from typing import Tuple

class UserRegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username: str, email: str, password: str) -> Tuple[bool, str]:
        if self.user_repository.get_user_by_email(email):
            return False, 'Email must be unique'
        
        if not self.validate_password(password):
            return False, 'Password does not meet security criteria'

        self.user_repository.create_user(username, email, password)
        return True, 'User registered successfully'

    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) < 8:
            return False
        return True