from werkzeug.security import generate_password_hash
from backend.repositories.user_account_management.user_repository import UserRepository
import re

class RegistrationService:
    
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> None:
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already registered")

        if not self.is_password_secure(password):
            raise ValueError("Password does not meet security criteria")

        hashed_password = generate_password_hash(password)
        user = User(email=email, password=hashed_password)
        self.user_repository.save_user(user)

    def is_password_secure(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True