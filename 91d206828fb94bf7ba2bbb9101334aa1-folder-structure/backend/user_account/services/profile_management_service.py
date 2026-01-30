# Epic Title: User Account Management
from repositories.profile_management_repository import ProfileManagementRepository

class ProfileManagementService:
    def __init__(self):
        self.profile_management_repository = ProfileManagementRepository()

    def get_profile(self, user_id: int) -> dict:
        profile = self.profile_management_repository.get_profile(user_id)
        if profile:
            return profile
        return {"error": "Failed to retrieve profile"}

    def update_profile(self, user_id: int, data: dict) -> dict:
        success = self.profile_management_repository.update_profile(user_id, data)
        if success:
            return {"message": "Profile updated successfully"}
        return {"error": "Failed to update profile"}