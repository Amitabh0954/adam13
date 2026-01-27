# Epic Title: User Account Management

from backend.database import db_session
from backend.models.user import User

class UserRepository:
    def create_user(self, email: str, password: str) -> User:
        new_user = User(email=email, password=password)
        db_session.add(new_user)
        db_session.commit()
        return new_user

    def get_user_by_email(self, email: str) -> User:
        return db_session.query(User).filter_by(email=email).first()
    
    def get_user_by_email_and_password(self, email: str, password: str) -> User:
        return db_session.query(User).filter_by(email=email, password=password).first()

    def update_user_password(self, user_id: int, new_password: str):
        user = db_session.query(User).filter_by(id=user_id).first()
        if user:
            user.password = new_password
            db_session.commit()