# Epic Title: User Registration

from typing import Optional
from user_account_management.repositories.user_repository import UserRepository
from user_account_management.models.user import User

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> Optional[User]:
        if self.user_repository.get_user_by_email(email):
            return None  # Email already exists

        # Here you would include the logic for password validation as per security criteria
        if not self.validate_password(password):
            return None  # Invalid password
        
        return self.user_repository.create_user(email, password)
    
    def validate_password(self, password: str) -> bool:
        # Implement a real validation based on security criteria
        return len(password) >= 8