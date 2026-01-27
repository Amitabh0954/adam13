# Epic Title: User Account Management

from backend.database import db_session
from backend.models.password_reset import PasswordReset

class PasswordResetRepository:
    def create_reset_token(self, user_id: int, token: str):
        reset_token = PasswordReset(user_id=user_id, token=token)
        db_session.add(reset_token)
        db_session.commit()

    def get_reset_token(self, token: str) -> PasswordReset:
        return db_session.query(PasswordReset).filter_by(token=token).first()

    def delete_reset_token(self, token: str):
        reset_token = self.get_reset_token(token)
        if reset_token:
            db_session.delete(reset_token)
            db_session.commit()