from backend.repositories.user_management.profile_repository import ProfileRepository
from backend.models.user import User

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()
    
    def get_profile(self, user_id: int) -> dict:
        user = self.profile_repository.find_by_id(user_id)
        if user:
            return {"email": user.email, "preferences": user.preferences}
        else:
            raise ValueError("User not found.")
    
    def update_profile(self, user_id: int, data: dict) -> dict:
        user = self.profile_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found.")
        
        if 'preferences' in data:
            user.preferences = data['preferences']
        self.profile_repository.update_user(user)
        return {"email": user.email, "preferences": user.preferences}