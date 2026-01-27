# Epic Title: User Account Management

from backend.database import db_session
from backend.user_account_management.models.user import User

class UserRepository:
    def get_user_by_email(self, email: str) -> User:
        return db_session.query(User).filter_by(email=email).first()
    
    def create_user(self, email: str, hashed_password: str):
        new_user = User(email=email, password=hashed_password)
        db_session.add(new_user)
        db_session.commit()