# Epic Title: User Account Management

from typing import Optional
from structured_logging import get_logger
from backend.user_account_management.repositories.profile_repository import ProfileRepository
from backend.user_account_management.models.profile import Profile

logger = get_logger(__name__)

class ProfileService:
    
    def __init__(self, profile_repository: ProfileRepository) -> None:
        self.profile_repository = profile_repository
    
    def get_profile(self, user_id: int) -> Optional[Profile]:
        return self.profile_repository.find_by_user_id(user_id)
    
    def update_profile(self, user_id: int, first_name: str, last_name: str, preferences: str) -> Optional[Profile]:
        profile = Profile(user_id=user_id, first_name=first_name, last_name=last_name, preferences=preferences)
        self.profile_repository.update_profile(profile)
        logger.info(f"Profile updated successfully for user_id: {user_id}")
        return profile