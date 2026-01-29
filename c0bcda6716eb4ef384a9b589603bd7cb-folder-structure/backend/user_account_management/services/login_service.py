# Epic Title: User Account Management

from datetime import datetime, timedelta
from typing import Optional
from structured_logging import get_logger
from backend.user_account_management.repositories.session_repository import SessionRepository
from backend.user_account_management.models.session import Session
from backend.user_account_management.repositories.user_repository import UserRepository
from backend.user_account_management.models.user import User

logger = get_logger(__name__)

class LoginService:
    
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository) -> None:
        self.user_repository = user_repository
        self.session_repository = session_repository
    
    def login(self, email: str, password: str) -> Optional[Session]:
        user = self.user_repository.find_by_email(email)
        if user is None or user.password != password:
            logger.error(f"Invalid login attempt for email: {email}")
            return None
        
        active_session = self.session_repository.get_active_session(user.id)
        if active_session:
            logger.info(f"User already logged in: {email}")
            return active_session
        
        new_session = Session(user.id)
        self.session_repository.add_session(new_session)
        logger.info(f"User logged in successfully: {email}")
        return new_session
    
    def logout(self, session_id: int) -> None:
        self.session_repository.end_session(session_id)
        logger.info(f"User with session ID {session_id} logged out.")