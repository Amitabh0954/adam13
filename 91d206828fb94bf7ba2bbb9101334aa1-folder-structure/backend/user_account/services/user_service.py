# Epic Title: User Account Management
from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> dict:
        if self.user_repository.exists_by_email(email):
            return {"error": "Email already exists"}

        hashed_password = generate_password_hash(password)
        user_id = self.user_repository.create_user(email, hashed_password)
        
        if user_id:
            return {"user_id": user_id, "message": "User registered successfully"}
        return {"error": "Failed to register user"}