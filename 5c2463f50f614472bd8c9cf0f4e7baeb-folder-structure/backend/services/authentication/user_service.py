from backend.repositories.authentication.user_repository import UserRepository
from backend.models.user import User
from backend.extensions import bcrypt

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def register_user(self, email: str, password: str):
        if not self.is_email_unique(email):
            raise ValueError("Email is already registered.")
        
        if not self.is_password_secure(password):
            raise ValueError("Password does not meet security criteria.")
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        self.user_repository.save_user(new_user)
    
    def is_email_unique(self, email: str) -> bool:
        return self.user_repository.find_by_email(email) is None
    
    def is_password_secure(self, password: str) -> bool:
        # Implement password security checks here (e.g., length, complexity)
        return len(password) >= 8