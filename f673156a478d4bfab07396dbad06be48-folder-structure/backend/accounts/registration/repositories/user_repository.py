# Epic Title: User Registration

from django.contrib.auth.models import User
from typing import Optional

class UserRepository:

    def create_user(self, email: str, password: str) -> User:
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(username=email)
        except User.DoesNotExist:
            return None