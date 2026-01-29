# Epic Title: User Account Management

from typing import Optional
from sqlalchemy.orm import Session
from backend.user_account_management.models.user import User

class UserRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_user(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()
    
    def find_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter_by(email=email).first()