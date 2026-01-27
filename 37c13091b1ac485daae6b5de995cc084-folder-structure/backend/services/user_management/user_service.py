from backend.repositories.user_management.user_repository import UserRepository
from backend.models.user import User
from backend.extensions import bcrypt

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def register_user(self, email: str, password: str):
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            raise ValueError("Email already registered")

        if not self._validate_password(password):
            raise ValueError("Password does not meet security criteria")

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        self.user_repository.save_user(new_user)
    
    def authenticate_user(self, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            raise ValueError("Invalid credentials")

    def _validate_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in "!@#$%^&*()_+" for char in password):
            return False
        return True

    def find_by_email(self, email: str) -> User:
        return self.user_repository.find_by_email(email)