# Epic Title: User Registration

from backend.accounts.repositories.user_repository import UserRepository
from backend.accounts.models.user import User

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register_user(self, email: str, password: str) -> User:
        existing_user = self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("A user with this email already exists")
        
        # Example password check; implement actual password validation in reality
        if len(password) < 8: 
            raise ValueError("The password must be at least 8 characters long")

        return self.user_repository.create_user(email, password)