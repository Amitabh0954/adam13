# Epic Title: User Account Management
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id: int, email: str):
        self.id = id
        self.email = email

    @staticmethod
    def get(user_id: int):
        from backend.repositories.user_repository import UserRepository
        user_repository = UserRepository()
        user_data = user_repository.get_user_by_id(user_id)
        if user_data:
            return User(user_data['id'], user_data['email'])
        return None