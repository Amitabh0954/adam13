# Epic Title: User Account Management
from repositories.user_management.user_repository import UserRepository
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login_user(self, email: str, password: str) -> tuple[UserMixin, str]:
        user_data = self.user_repository.get_user_by_email(email)
        
        if user_data and check_password_hash(user_data['password'], password):
            user = UserMixin()
            user.id = user_data['id']
            return user, None
        
        return None, "Invalid email or password"