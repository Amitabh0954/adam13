# Epic Title: Profile Management

from django.contrib.auth.models import User
from typing import Optional

class ProfileRepository:

    def update_user_profile(self, user: User, first_name: str, last_name: str, email: str) -> User:
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return user

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None