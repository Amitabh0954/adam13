# Epic Title: Profile Management

from backend.repositories.user_repository import UserRepository
from typing import Tuple, Optional

class UserProfileService:
    def __init__(self):
        self.user_repository = UserRepository()

    def update_profile(self, user_id: int, **kwargs) -> Tuple[bool, str]:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return False, 'User not found'
        
        for field, value in kwargs.items():
            if hasattr(user, field):
                setattr(user, field, value)
        
        user.save()
        return True, 'Profile updated successfully'

    def get_user_profile(self, user_id: int) -> Optional[dict]:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return None
        
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return user_data