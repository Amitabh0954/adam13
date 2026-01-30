# Epic Title: Profile Management

from accounts.profile_management.repositories.profile_repository import ProfileRepository
from django.contrib.auth.models import User
from typing import Optional

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def update_profile(self, user: User, first_name: str, last_name: str, email: str) -> User:
        return self.profile_repository.update_user_profile(user, first_name, last_name, email)

    def get_profile(self, user_id: int) -> Optional[User]:
        return self.profile_repository.get_user_by_id(user_id)