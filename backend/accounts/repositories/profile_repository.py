# Epic Title: Profile Management

from backend.accounts.models.profile import Profile
from backend.accounts.models.user import User

class ProfileRepository:
    def get_profile_by_user(self, user: User) -> Profile:
        return Profile.objects.filter(user=user).first()

    def update_profile(self, user: User, first_name: str, last_name: str, preferences: dict) -> Profile:
        profile = self.get_profile_by_user(user)
        if not profile:
            profile = Profile(user=user)
        
        profile.first_name = first_name
        profile.last_name = last_name
        profile.preferences = preferences
        profile.save()
        return profile