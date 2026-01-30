# Epic Title: User Account Management
from repositories.user_management.user_repository import UserRepository
import re
import bcrypt

class RegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> dict:
        if self.user_repository.exists_by_email(email):
            return {"error": "Email already in use"}

        if not self._validate_password(password):
            return {"error": "Password does not meet security criteria"}

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_id = self.user_repository.create_user(email, hashed_password)
        
        if user_id:
            return {"user_id": user_id, "message": "User registered successfully"}
        
        return {"error": "Failed to register user"}

    def _validate_password(self, password: str) -> bool:
        # Password validation criteria: At least 8 characters, one uppercase, one lowercase, one digit
        return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', password))