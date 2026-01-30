# Epic Title: User Login

from backend.accounts.models.session import Session
from backend.accounts.models.user import User
from django.utils.crypto import get_random_string

class SessionRepository:
    def create_session(self, user: User) -> Session:
        session_token = get_random_string(50)
        session = Session(user=user, session_token=session_token)
        session.save()
        return session

    def get_session_by_token(self, token: str) -> Session:
        return Session.objects.filter(session_token=token).first()

    def invalidate_session(self, session: Session) -> None:
        session.delete()