# Epic Title: User Account Management
from repositories.user_repository import UserRepository
import re
import hashlib

class UserRegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> dict:
        if not self.is_valid_email(email):
            return {"error": "Invalid email format"}
        
        if not self.is_strong_password(password):
            return {"error": "Password does not meet security criteria"}
        
        if self.user_repository.email_exists(email):
            return {"error": "Email already exists"}
        
        hashed_password = self.hash_password(password)
        user_id = self.user_repository.create_user(email, hashed_password)
        return {"user_id": user_id, "message": "User registered successfully"}
    
    def is_valid_email(self, email: str) -> bool:
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.match(email_regex, email) is not None
    
    def is_strong_password(self, password: str) -> bool:
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)
    
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()