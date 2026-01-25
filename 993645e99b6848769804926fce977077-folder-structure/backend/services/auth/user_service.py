import re
from backend.repositories.auth.user_repository import UserRepository
from backend.models.user import User

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> None:
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already exists")

        if not self.is_password_strong(password):
            raise ValueError("Password does not meet security criteria")

        new_user = User(email=email, password=password)
        self.user_repository.save_user(new_user)

    @staticmethod
    def is_password_strong(password: str) -> bool:
        return len(password) >= 8 and bool(re.search(r"\d", password)) and bool(re.search(r"[A-Z]", password))