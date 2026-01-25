from backend.repositories.auth.login_repository import LoginRepository
from backend.models.user import User
import datetime

class LoginService:
    MAX_LOGIN_ATTEMPTS = 5

    def __init__(self):
        self.login_repository = LoginRepository()

    def authenticate(self, email: str, password: str) -> User:
        user = self.login_repository.get_user_by_email(email)
        
        if not user:
            raise ValueError("Invalid email or password")

        if user.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
            raise ValueError("Account locked due to too many invalid login attempts")
        
        if user.password != password:
            self.login_repository.update_login_attempts(user)
            raise ValueError("Invalid email or password")
        
        self.login_repository.reset_login_attempts(user)
        return user