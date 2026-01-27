# Epic Title: User Account Management

from backend.database import db_session
from backend.user_account_management.models.password_reset_token import PasswordResetToken
from datetime import datetime

class PasswordResetRepository:
    def save_password_reset_token(self, user_id: int, token: str):
        password_reset_token = PasswordResetToken(user_id=user_id, token=token, created_at=datetime.utcnow())
        db_session.add(password_reset_token)
        db_session.commit()

    def invalidate_password_reset_token(self, user_id: int):
        db_session.query(PasswordResetToken).filter_by(user_id=user_id).delete()
        db_session.commit()