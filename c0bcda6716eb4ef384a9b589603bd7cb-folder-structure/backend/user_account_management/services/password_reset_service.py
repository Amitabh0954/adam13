# Epic Title: User Account Management

from typing import Optional
from structured_logging import get_logger
from backend.user_account_management.repositories.password_reset_repository import PasswordResetRepository
from backend.user_account_management.repositories.user_repository import UserRepository
from backend.user_account_management.models.password_reset import PasswordReset
from backend.user_account_management.models.user import User
import uuid
import datetime

logger = get_logger(__name__)

class PasswordResetService:
    
    def __init__(self, user_repository: UserRepository, password_reset_repository: PasswordResetRepository) -> None:
        self.user_repository = user_repository
        self.password_reset_repository = password_reset_repository
    
    def create_reset_request(self, email: str) -> Optional[str]:
        user = self.user_repository.find_by_email(email)
        if user is None:
            logger.error(f"Password reset requested for non-existent email: {email}")
            return None
        
        token = str(uuid.uuid4())
        reset_request = PasswordReset(user_id=user.id, token=token)
        self.password_reset_repository.add_reset_request(reset_request)
        
        # Here you would send an email with the reset link containing the token
        logger.info(f"Password reset token created for user: {email}")
        
        return token
    
    def reset_password(self, token: str, new_password: str) -> bool:
        reset_request = self.password_reset_repository.find_by_token(token)
        if reset_request is None:
            logger.error(f"Invalid or expired password reset token: {token}")
            return False
        
        if reset_request.expires_at < datetime.datetime.utcnow():
            self.password_reset_repository.delete_reset_request(token)
            logger.error(f"Expired password reset token: {token}")
            return False
        
        user = self.user_repository.find_by_email(reset_request.user_id)
        if user is None:
            logger.error(f"User not found for reset token: {token}")
            return False
        
        user.password = new_password
        self.password_reset_repository.delete_reset_request(token)
        logger.info(f"Password reset successful for token: {token}")
        return True