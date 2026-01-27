# Epic Title: User Account Management

from backend.repositories.user_account.user_repository import UserRepository

class ProfileService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_profile(self, user_id: int) -> dict:
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return {
                'email': user.email,
                'name': user.name,
                'preferences': user.preferences
            }
        return None

    def update_profile(self, user_id: int, data: dict) -> dict:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            return {'status': 'error', 'message': 'User not found'}

        user.name = data.get('name', user.name)
        user.preferences = data.get('preferences', user.preferences)
        self.user_repository.update_user(user)

        return {'status': 'success'}