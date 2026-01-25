import time
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from backend.repositories.user_account_management.user_repository import UserRepository
import logging

logger = logging.getLogger(__name__)

class LoginService:
    
    def __init__(self):
        self.user_repository = UserRepository()
        self.failed_attempts = {}
        self.lock_time = 300  # Lock for 5 minutes

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        
        if not user:
            raise ValueError("Invalid email or password")

        if email in self.failed_attempts:
            block_end_time, attempts = self.failed_attempts[email]
            if attempts >= 5 and time.time() < block_end_time:
                raise ValueError("Too many failed attempts. Try again later.")

        if check_password_hash(user.password, password):
            if email in self.failed_attempts:
                del self.failed_attempts[email]
            return user
        else:
            if email not in self.failed_attempts:
                self.failed_attempts[email] = (time.time() + self.lock_time, 1)
            else:
                block_end_time, attempts = self.failed_attempts[email]
                self.failed_attempts[email] = (block_end_time, attempts + 1)
            raise ValueError("Invalid email or password")