from backend.repositories.auth.profile_repository import ProfileRepository

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_user_profile(self, user_id: int) -> dict:
        user = self.profile_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        return {
            "id": user.id,
            "email": user.email,
            "preferences": user.preferences
        }

    def update_user_profile(self, user_id: int, data: dict) -> None:
        user = self.profile_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        user.email = data.get("email", user.email)
        user.preferences = data.get("preferences", user.preferences)
        
        self.profile_repository.update_user(user)