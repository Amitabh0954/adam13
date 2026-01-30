# Epic Title: User Account Management
from repositories.profile_repository import ProfileRepository

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_profile(self, user_id: int) -> dict | None:
        return self.profile_repository.get_profile(user_id)

    def update_profile(self, user_id: int, data: dict) -> dict:
        if self.profile_repository.update_profile(user_id, data):
            return {"message": "Profile updated successfully"}
        return {"error": "Failed to update profile"}