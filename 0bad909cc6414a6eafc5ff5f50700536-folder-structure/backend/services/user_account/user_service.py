# Epic Title: User Account Management

import re
from typing import Optional
from backend.repositories.user_account.user_repository import UserRepository
import bcrypt

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Za-z]", password):
            return False
        if not re.search(r"[0-9]", password):
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