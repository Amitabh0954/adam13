# Epic Title: User Account Management
from repositories.user_repository import UserRepository

class ProfileManagementService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_profile(self, user_id: int) -> dict:
        return self.user_repository.get_user_profile(user_id)

    def update_profile(self, user_id: int, data: dict) -> dict:
        updated = self.user_repository.update_user_profile(user_id, data)
        if updated:
            return {"message": "Profile updated successfully"}
        return {"error": "Profile update failed"}