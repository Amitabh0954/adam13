# Epic Title: User Account Management

from backend.user_account_management.repositories.profile_repository import ProfileRepository
from typing import Dict

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def update_profile(self, user_id: int, data: Dict) -> Dict[str, str]:
        if not data:
            return {'status': 'error', 'message': 'No data provided'}

        self.profile_repository.update_profile(user_id, data)
        return {'status': 'success', 'message': 'Profile updated successfully'}