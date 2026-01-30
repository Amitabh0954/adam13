# Epic Title: User Registration

from account.models.user import User
from typing import Optional

class UserRepository:

    def create_user(self, email: str, username: str, password: str) -> User:
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_user_by_username(self, username: str) -> Optional[User]:
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None