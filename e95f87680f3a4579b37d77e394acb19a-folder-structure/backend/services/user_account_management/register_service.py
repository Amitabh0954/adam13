# Epic Title: User Account Management
from repositories.user_repository import UserRepository
import bcrypt

class RegisterService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> dict:
        if self.user_repository.get_user_by_email(email):
            return {"error": "Email already exists"}

        if not self._is_password_secure(password):
            return {"error": "Password does not meet security criteria"}

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.user_repository.create_user(email, hashed_password)
        return {"message": "User registered successfully"}

    def _is_password_secure(self, password: str) -> bool:
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)