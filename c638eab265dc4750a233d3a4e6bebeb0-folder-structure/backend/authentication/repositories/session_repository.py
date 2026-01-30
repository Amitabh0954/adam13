# Epic Title: User Login

from authentication.models.session import Session
from django.contrib.auth.models import User
from typing import Optional

class SessionRepository:

    def create_session(self, user: User, session_key: str) -> Session:
        session = Session(user=user, session_key=session_key)
        session.save()
        return session

    def get_session_by_key(self, session_key: str) -> Optional[Session]:
        try:
            return Session.objects.get(session_key=session_key)
        except Session.DoesNotExist:
            return None

    def invalidate_session(self, session_key: str) -> None:
        session = self.get_session_by_key(session_key)
        if session:
            session.is_active = False
            session.save()

    def validate_session(self, session_key: str) -> bool:
        session = self.get_session_by_key(session_key)
        if session and session.is_active:
            session.last_activity = timezone.now()
            session.save()
            return True
        return False