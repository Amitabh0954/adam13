# Epic Title: User Account Management
from backend.repositories.profile_repository import ProfileRepository
from backend.models.user_account.profile import Profile

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_profile(self, user_id: int) -> dict:
        profile_data = self.profile_repository.get_profile(user_id)
        if not profile_data:
            return {"error": "Profile not found"}

        return profile_data

    def update_profile(self, user_id: int, first_name: str, last_name: str, email: str, preferences: str) -> dict:
        if not Profile.validate_email(email):
            return {"error": "Invalid email format"}

        profile = Profile(user_id, first_name, last_name, email, preferences)
        success = self.profile_repository.update_profile(profile)
        if not success:
            return {"error": "Failed to update profile"}

        return {"message": "Profile updated successfully"}