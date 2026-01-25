from backend.repositories.user_account_management.user_repository import UserRepository

class ProfileService:
    
    def __init__(self):
        self.user_repository = UserRepository()

    def update_profile(self, user_id: int, name: str, preferences: str) -> None:
        self.user_repository.update_user(user_id, name, preferences)