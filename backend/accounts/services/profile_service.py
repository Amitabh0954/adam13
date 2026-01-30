# Epic Title: Profile Management

from backend.accounts.repositories.user_repository import UserRepository
from backend.accounts.repositories.profile_repository import ProfileRepository
from backend.accounts.models.profile import Profile
import logging

logger = logging.getLogger(__name__)

class ProfileService:
    def __init__(self, user_repository: UserRepository, profile_repository: ProfileRepository) -> None:
        self.user_repository = user_repository
        self.profile_repository = profile_repository
    
    def update_user_profile(self, email: str, first_name: str, last_name: str, preferences: dict) -> Profile:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("No user found with this email")
        
        profile = self.profile_repository.update_profile(user, first_name, last_name, preferences)
        logger.info(f"Profile updated for user {email}")
        return profile
    
    def get_user_profile(self, email: str) -> Profile:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("No user found with this email")
        
        profile = self.profile_repository.get_profile_by_user(user)
        logger.info(f"Retrieved profile for user {email}")
        return profile