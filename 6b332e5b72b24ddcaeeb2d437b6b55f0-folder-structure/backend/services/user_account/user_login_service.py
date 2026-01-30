# Epic Title: User Login

from django.contrib.auth import authenticate
from backend.repositories.user_repository import UserRepository
from typing import Tuple, Optional

class UserLoginService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.login_attempts = {}
        self.MAX_ATTEMPTS = 5
        self.TIMEOUT = 300  # 5 minutes in seconds

    def login_user(self, email: str, password: str) -> Tuple[bool, str, Optional[dict]]:
        if email not in self.login_attempts:
            self.login_attempts[email] = 0

        if self.login_attempts[email] >= self.MAX_ATTEMPTS:
            return False, 'Account locked due to too many failed login attempts', None

        user = authenticate(username=email, password=password)
        if user is not None:
            self.login_attempts[email] = 0  # Reset count on successful login
            user_data = {
                'username': user.username,
                'email': user.email,
            }
            return True, 'Login successful', user_data
        else:
            self.login_attempts[email] += 1
            return False, 'Invalid login credentials', None

    def logout_user(self, user) -> str:
        # Implement logout logic if using a session or token mechanism
        return 'Logout successful'