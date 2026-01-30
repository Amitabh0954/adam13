# Epic Title: User Login

from authentication.repositories.session_repository import SessionRepository
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from typing import Optional

class AuthenticationService:
    def __init__(self):
        self.session_repository = SessionRepository()

    def login(self, username: str, password: str, session_key: str) -> Optional[User]:
        user = authenticate(username=username, password=password)
        if user:
            self.session_repository.create_session(user, session_key)
            return user
        return None

    def validate_session(self, session_key: str) -> bool:
        return self.session_repository.validate_session(session_key)

    def logout(self, session_key: str) -> None:
        self.session_repository.invalidate_session(session_key)