# Epic Title: User Registration

from user_account_management.models.user import User
from django.contrib.auth.hashers import make_password
from typing import Optional

class UserRepository:

    def create_user(self, username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password=make_password(password))
        user.save()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None