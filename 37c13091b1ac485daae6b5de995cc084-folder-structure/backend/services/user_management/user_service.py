from backend.repositories.user_management.user_repository import UserRepository
from backend.models.user import User
from backend.extensions import bcrypt

class UserService:
    # Inline comment referencing the Epic Title
    # Epic Title: Shopping Cart Functionality

    def __init__(self):
        self.user_repository = UserRepository()
    
    def register_user(self, email: str, password: str):
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            raise ValueError("Email already registered")

        if not self._validate_password(password):
            raise ValueError("Password does not meet security criteria")

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password, is_admin=False)
        self.user_repository.save_user(new_user)
    
    def authenticate_user(self, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            raise ValueError("Invalid credentials")

    def reset_password(self, email: str, new_password: str):
        user = self.user_repository.find_by_email(email)
        if not user:
            raise ValueError("Email not registered")

        if not self._validate_password(new_password):
            raise ValueError("Password does not meet security criteria")

        user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        self.user_repository.update_user(user)

    def update_profile(self, user_id: int, data: dict):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not