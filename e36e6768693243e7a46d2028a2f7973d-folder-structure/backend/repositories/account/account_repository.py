# Epic Title: User Account Management

from backend.database import db_session
from backend.models.user import User
from backend.models.password_reset import PasswordReset
from datetime import datetime

class AccountRepository:
    def get_user_by_email(self, email: str) -> User:
        return db_session.query(User).filter_by(email=email).first()

    def create_user(self, email: str, password: str) -> User:
        new_user = User(email=email, password=password)
        db_session.add(new_user)
        db_session.commit()
        return new_user

    def update_user_password(self, user_id: int, password: str):
        user = db_session.query(User).filter_by(id=user_id).first()
        if user:
            user.password = password
            db_session.commit()

    def save_password_reset_token(self, user_id: int, token: str, expiry_time: datetime):
        password_reset = PasswordReset(user_id=user_id, token=token, expiry_time=expiry_time)
        db_session.add(password_reset)
        db_session.commit()

    def get_password_reset_request(self, token: str) -> PasswordReset:
        return db_session.query(PasswordReset).filter_by(token=token).first()

    def delete_password_reset_request(self, token: str):
        reset_request = db_session.query(PasswordReset).filter_by(token=token).first()
        if reset_request:
            db_session.delete(reset_request)
            db_session.commit()