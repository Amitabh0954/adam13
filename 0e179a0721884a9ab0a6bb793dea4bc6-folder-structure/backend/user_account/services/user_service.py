# Epic Title: User Account Management
from repositories.user_repository import UserRepository
import re
import bcrypt

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> dict:
        if not self.is_email_valid(email):
            return {"error": "Invalid email format"}
        
        if not self.is_password_secure(password):
            return {"error": "Password does not meet security criteria"}
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        if self.user_repository.is_email_taken(email):
            return {"error": "Email is already registered"}
        
        user_id = self.user_repository.create_user(email, hashed_password)
        return {"user_id": user_id, "message": "User registered successfully"}
    
    def is_email_valid(self, email: str) -> bool:
        return re.match(r'[^@]+@[^@]+\.[^@]+', email) is not None
    
    def is_password_secure(self, password: str) -> bool:
        return (
            len(password) >= 8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[\W_]', password)
        )