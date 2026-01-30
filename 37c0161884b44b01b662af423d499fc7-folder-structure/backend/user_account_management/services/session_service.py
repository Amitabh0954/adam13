# Epic Title: User Login

import uuid
from typing import Optional
from user_account_management.repositories.user_repository import UserRepository
from user_account_management.repositories.session_repository import SessionRepository
from user_account_management.models.user import User
from user_account_management.models.session import Session

class SessionService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.session_repository = SessionRepository()

    def login_user(self, email: str, password: str) -> Optional[Session]:
        user = self.user_repository.get_user_by_email(email)
        if user and user.password == password:  # Simplified password check
            session_id = str(uuid.uuid4())
            return self.session_repository.create_session(user, session_id)
        return None

    def validate_session(self, session_id: str) -> bool:
        session = self.session_repository.get_session_by_id(session_id)
        if session:
            self.session_repository.update_last_activity(session_id)
            return True
        return False