# Epic Title: Profile Management

from account.models.user import User
from typing import Optional

class ProfileRepository:

    def update_user(self, user: User, username: str, first_name: str, last_name: str, email: str) -> Optional[User]:
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return user