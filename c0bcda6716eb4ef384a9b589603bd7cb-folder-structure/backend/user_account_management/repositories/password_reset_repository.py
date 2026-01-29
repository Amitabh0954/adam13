# Epic Title: User Account Management

from typing import Optional
from sqlalchemy.orm import Session
from backend.user_account_management.models.password_reset import PasswordReset

class PasswordResetRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_reset_request(self, password_reset: PasswordReset) -> None:
        self.session.add(password_reset)
        self.session.commit()

    def find_by_token(self, token: str) -> Optional[PasswordReset]:
        return self.session.query(PasswordReset).filter_by(token=token).first()

    def delete_reset_request(self, token: str) -> None:
        request = self.session.query(PasswordReset).filter_by(token=token).first()
        if request:
            self.session.delete(request)
            self.session.commit()