# Epic Title: Profile Management

from account.repositories.profile_repository import ProfileRepository
from account.models.user import User
from typing import Optional

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def update_profile(self, user: User, username: str, first_name: str, last_name: str, email: str) -> Optional[User]:
        return self.profile_repository.update_user(user, username, first_name, last_name, email)