# Epic Title: User Account Management

from backend.database import db_session
from backend.models.user import User

class AccountRepository:
    def get_user_by_email(self, email: str) -> User:
        return db_session.query(User).filter_by(email=email).first()

    def create_user(self, email: str, password: str) -> User:
        new_user = User(email=email, password=password)
        db_session.add(new_user)
        db_session.commit()
        return new_user