# Epic Title: Profile Management

from user_account_management.models.user import User
from django.contrib.auth.hashers import make_password, check_password
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

    def validate_user(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email)
        if user and check_password(password, user.password):
            return user
        return None

    def update_user_profile(self, user: User, **kwargs) -> User:
        for attr, value in kwargs.items():
            setattr(user, attr, value)
        user.save()
        return user