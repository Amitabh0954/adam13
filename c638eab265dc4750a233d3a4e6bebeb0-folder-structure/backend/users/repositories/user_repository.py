# Epic Title: User Registration

from users.models.user import User
from typing import Optional

class UserRepository:

    def create_user(self, username: str, email: str, password: str) -> User:
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None