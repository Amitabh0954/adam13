# Epic Title: Profile Management

from user_account_management.repositories.user_repository import UserRepository
from user_account_management.models.user import User
from typing import Optional

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username: str, email: str, password: str) -> Optional[User]:
        if self.user_repository.get_user_by_email(email):
            return None
        return self.user_repository.create_user(username, email, password)

    def login_user(self, email: str, password: str) -> Optional[User]:
        return self.user_repository.validate_user(email, password)
    
    def update_user_profile(self, email: str, **kwargs) -> Optional[User]:
        user = self.user_repository.get_user_by_email(email)
        if user:
            return self.user_repository.update_user_profile(user, **kwargs)
        return None