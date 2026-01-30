# Epic Title: User Login

from backend.accounts.repositories.user_repository import UserRepository
from backend.accounts.repositories.session_repository import SessionRepository
from backend.accounts.models.user import User
from backend.accounts.models.session import Session
import logging

logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository) -> None:
        self.user_repository = user_repository
        self.session_repository = session_repository

    def login(self, email: str, password: str) -> Session:
        user = self.user_repository.get_user_by_email(email)
        if not user or user.password != password:
            logger.warning("Invalid login attempt for email: %s", email)
            raise ValueError("Invalid username or password")
        
        session = self.session_repository.create_session(user)
        return session

    def validate_session(self, token: str) -> User:
        session = self.session_repository.get_session_by_token(token)
        if not session or not session.is_active():
            raise ValueError("Session is invalid or expired")

        session.last_activity = datetime.now()
        session.save()
        return session.user
        
    def logout(self, token: str) -> None:
        session = self.session_repository.get_session_by_token(token)
        if session:
            self.session_repository.invalidate_session(session)