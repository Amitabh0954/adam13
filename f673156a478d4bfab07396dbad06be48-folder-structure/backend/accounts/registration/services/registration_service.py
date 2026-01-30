# Epic Title: User Registration

from accounts.registration.repositories.user_repository import UserRepository
from django.contrib.auth.models import User
from typing import Optional

class RegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str, confirm_password: str) -> Optional[User]:
        if password != confirm_password:
            return None

        if len(password) < 8:
            return None

        if self.user_repository.get_user_by_email(email):
            return None

        return self.user_repository.create_user(email, password)