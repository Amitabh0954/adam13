# Epic Title: Profile Management

from typing import Optional
from user_account_management.models.profile import Profile
from user_account_management.models.user import User

class ProfileRepository:

    def get_profile_by_user(self, user: User) -> Optional[Profile]:
        try:
            return Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return None

    def create_or_update_profile(self, user: User, first_name: str, last_name: str, date_of_birth: Optional[str]) -> Profile:
        profile, created = Profile.objects.update_or_create(
            user=user,
            defaults={'first_name': first_name, 'last_name': last_name, 'date_of_birth': date_of_birth, 'updated_at': timezone.now()},
        )
        return profile