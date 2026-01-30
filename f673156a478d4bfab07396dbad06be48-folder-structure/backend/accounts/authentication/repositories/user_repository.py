# Epic Title: User Login

from django.contrib.auth.models import User
from typing import Optional

class UserRepository:

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(username=email)
        except User.DoesNotExist:
            return None