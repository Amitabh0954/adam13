# Epic Title: User Login

from typing import Optional
from django.utils import timezone
from user_account_management.models.session import Session
from user_account_management.models.user import User

class SessionRepository:
    
    def create_session(self, user: User, session_id: str) -> Session:
        session = Session(user=user, session_id=session_id)
        session.save()
        return session

    def get_session_by_id(self, session_id: str) -> Optional[Session]:
        try:
            return Session.objects.get(session_id=session_id)
        except Session.DoesNotExist:
            return None

    def update_last_activity(self, session_id: str) -> bool:
        session = self.get_session_by_id(session_id)
        if session:
            session.last_activity = timezone.now()
            session.save()
            return True
        return False