# Epic Title: User Account Management

from typing import Optional
from sqlalchemy.orm import Session as OrmSession
from backend.user_account_management.models.session import Session

class SessionRepository:
    
    def __init__(self, session: OrmSession) -> None:
        self.session = session
    
    def add_session(self, user_session: Session) -> None:
        self.session.add(user_session)
        self.session.commit()

    def get_active_session(self, user_id: int) -> Optional[Session]:
        return self.session.query(Session).filter_by(user_id=user_id, end_time=None).first()

    def end_session(self, session_id: int) -> None:
        session = self.session.query(Session).filter_by(id=session_id).first()
        if session:
            session.end_time = datetime.datetime.utcnow()
            self.session.commit()