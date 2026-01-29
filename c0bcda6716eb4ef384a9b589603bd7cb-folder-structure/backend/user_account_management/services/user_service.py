# Epic Title: User Account Management

from typing import Optional
from structured_logging import get_logger
from backend.user_account_management.repositories.user_repository import UserRepository
from backend.user_account_management.models.user import User

logger = get_logger(__name__)

class UserService:
    
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
    
    def register_user(self, email: str, password: str) -> Optional[User]:
        if not self._is_valid_email(email):
            logger.error(f"Invalid email format: {email}")
            return None
        
        if not self._is_valid_password(password):
            logger.error(f"Password does not meet criteria.")
            return None
        
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            logger.error(f"Email already used: {email}")
            return None
        
        user = User(email, password)
        self.user_repository.add_user(user)
        logger.info(f"User registered successfully: {email}")
        return user
    
    def _is_valid_email(self, email: str) -> bool:
        # Basic email regex check (could be extended)
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
    
    def _is_valid_password(self, password: str) -> bool:
        # Basic password criteria check (could be extended)
        return len(password) >= 8