# Epic Title: Profile Management

from repositories.user_account.user_repository import UserRepository

class ProfileManagementService:
    def __init__(self):
        self.user_repository = UserRepository()

    def update_profile(self, data: dict) -> dict:
        user_id = data['user_id']
        updated_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
        self.user_repository.update_user_profile(user_id, updated_data)
        return {"msg": "Profile updated successfully"}