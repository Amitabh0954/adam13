from backend.repositories.user_account_management.profile_repository import ProfileRepository

class ProfileManagementService:

    def __init__(self):
        self.profile_repository = ProfileRepository()

    def get_profile(self, user_id: int):
        return self.profile_repository.get_profile(user_id)

    def update_profile(self, user_id: int, data: dict):
        return self.profile_repository.update_profile(user_id, data)