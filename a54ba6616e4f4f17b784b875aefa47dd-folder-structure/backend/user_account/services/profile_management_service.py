# Epic Title: User Account Management
from repositories.profile_repository import ProfileRepository
import re

class ProfileManagementService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def update_profile(self, user_id: int, name: str, email: str, preferences: dict) -> dict:
        if not self.is_valid_email(email):
            return {"error": "Invalid email format"}

        if self.profile_repository.email_exists(user_id, email):
            return {"error": "Email already exists"}

        updated = self.profile_repository.update_profile(user_id, name, email, preferences)
        if updated:
            return {"message": "Profile updated successfully"}
        return {"error": "Failed to update profile"}

    def is_valid_email(self, email: str) -> bool:
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.match(email_regex, email) is not None