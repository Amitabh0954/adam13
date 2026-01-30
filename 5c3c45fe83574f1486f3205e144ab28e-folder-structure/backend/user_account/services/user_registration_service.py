# Epic Title: User Account Management
import re
from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash

class UserRegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, data: dict) -> dict:
        email = data.get('email')
        password = data.get('password')
        
        if not self._is_valid_email(email):
            return {"error": "Invalid email format"}

        if not self._is_valid_password(password):
            return {"error": "Password does not meet security criteria"}

        if self.user_repository.is_email_taken(email):
            return {"error": "Email is already registered"}

        hashed_password = generate_password_hash(password)
        user_id = self.user_repository.create_user(email, hashed_password)
        return {"user_id": user_id}

    def _is_valid_email(self, email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def _is_valid_password(self, password: str) -> bool:
        return len(password) >= 8 and re.search(r"[A-Za-z]", password) and re.search(r"\d", password)