# Epic Title: User Account Management

from typing import Optional
from backend.repositories.user_account.user_repository import UserRepository
import bcrypt

class UserService:
    MAX_FAILED_ATTEMPTS = 5  # configurable
    FAILED_ATTEMPT_INTERVAL_MINUTES = 15  # configurable

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        return True

    def register_user(self, email: str, password: str) -> Optional[str]:
        if not self.validate_password(password):
            return "Password must be at least 8 characters long and include both letters and numbers."
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if self.user_repository.find_user_by_email(email):
            return "Email already registered"

        self.user_repository.create_user(email, hashed_password.decode('utf-8'))
        return None

    def authenticate_user(self, email: str, password: str) -> Optional[str]:
        failed_attempts = self.user_repository.count_recent_failed_attempts(email, self.FAILED_ATTEMPT_INTERVAL_MINUTES)
        if failed_attempts >= self.MAX_FAILED_ATTEMPTS:
            return "Too many failed login attempts. Please try again later."
        
        user = self.user_repository.find_user_by_email(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            # Placeholder for session creation logic
            return None
        else:
            self.user_repository.register_failed_attempt(email)
            return "Invalid email or password"