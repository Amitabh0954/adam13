from backend.repositories.user_account_management.user_repository import UserRepository

class ProfileService:
    
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_profile(self, user_id: int) -> dict:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        return {
            "email": user.email,
            "name": user.name,
            "preferences": user.preferences
        }

    def update_user_profile(self, user_id: int, name: str = None, preferences: str = None) -> None:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        if name:
            user.name = name
        if preferences:
            user.preferences = preferences
        
        self.user_repository.save_user(user)