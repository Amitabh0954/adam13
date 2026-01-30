# Epic Title: User Account Management
from repositories.user_repository import UserRepository
import hashlib

class UserLoginService:
    def __init__(self):
        self.user_repository = UserRepository()
        
    def login_user(self, email: str, password: str) -> dict:
        if not self.user_repository.email_exists(email):
            return {"error": "Invalid email or password"}
        
        hashed_password = self.hash_password(password)
        user = self.user_repository.get_user_by_email_and_password(email, hashed_password)
        
        if not user:
            return {"error": "Invalid email or password"}
        
        return {"user_id": user['id'], "message": "Login successful"}
    
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()