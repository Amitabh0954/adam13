# Epic Title: Profile Management

from typing import Optional
from user_account_management.repositories.profile_repository import ProfileRepository
from user_account_management.repositories.user_repository import UserRepository
from user_account_management.models.profile import Profile
from user_account_management.models.user import User

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()
        self.user_repository = UserRepository()

    def update_profile(self, email: str, first_name: str, last_name: str, date_of_birth: Optional[str]) -> Optional[Profile]:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return None

        return self.profile_repository.create_or_update_profile(user, first_name, last_name, date_of_birth)