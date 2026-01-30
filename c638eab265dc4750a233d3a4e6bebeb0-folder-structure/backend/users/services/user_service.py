# Epic Title: User Registration

from users.repositories.user_repository import UserRepository
from users.models.user import User
from typing import Optional

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username: str, email: str, password: str) -> Optional[User]:
        if self.user_repository.get_user_by_email(email):
            return None
        return self.user_repository.create_user(username, email, password)