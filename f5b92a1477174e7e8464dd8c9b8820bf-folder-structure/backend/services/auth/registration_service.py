from werkzeug.security import generate_password_hash
from backend.repositories.user_account_management.user_repository import UserRepository
from backend.models.user import User
import re

class RegistrationService:
    
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> None:
        if not self._is_valid_email(email):
            raise ValueError("Invalid email address")
        
        if not self._is_valid_password(password):
            raise ValueError("Password does not meet security criteria")

        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already in use")

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        self.user_repository.save_user(new_user)

    def _is_valid_email(self, email: str) -> bool:
        pattern = r"(^[-!#$%&'*+/0-9=?A-Z^_a-z{|}~]+(\.[-!#$%&'*+/0-9=?A-Z^_a-z`{|}~]+)*"
        "@([A-Z0-9a-z]([-A-Z0-9a-z]{0,61}[A-Z0-9a-z])?\.)+[A-Za-z]{2,6}$)"
        return bool(re.match(pattern, email))

    def _is_valid_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[@$!%*?&#]", password):
            return False
        return True