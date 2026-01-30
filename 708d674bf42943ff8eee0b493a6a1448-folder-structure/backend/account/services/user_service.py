# Epic Title: User Registration

from account.repositories.user_repository import UserRepository
from account.models.user import User
from typing import Optional

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, username: str, password: str) -> Optional[User]:
        if self.user_repository.get_user_by_email(email) or self.user_repository.get_user_by_username(username):
            return None
        return self.user_repository.create_user(email, username, password)