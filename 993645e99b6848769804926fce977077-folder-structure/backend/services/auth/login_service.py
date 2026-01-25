from werkzeug.security import check_password_hash
from backend.repositories.user_account_management.user_repository import UserRepository
from flask_login import UserMixin

class LoginService:
    
    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            return user
        return None