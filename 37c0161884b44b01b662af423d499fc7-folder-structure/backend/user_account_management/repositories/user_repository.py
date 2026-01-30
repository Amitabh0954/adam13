# Epic Title: User Registration

from typing import Optional
from user_account_management.models.user import User

class UserRepository:
    
    def create_user(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        user.save()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None