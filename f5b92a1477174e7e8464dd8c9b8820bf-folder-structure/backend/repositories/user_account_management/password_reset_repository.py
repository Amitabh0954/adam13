import logging
from datetime import datetime, timedelta
from backend.models.password_reset import PasswordReset
from backend.database import db

logger = logging.getLogger(__name__)

class PasswordResetRepository:
    
    def create_password_reset(self, user_id: int, token: str) -> None:
        expires_at = datetime.utcnow() + timedelta(days=1)
        password_reset = PasswordReset(user_id=user_id, token=token, expires_at=expires_at)
        db.session.add(password_reset)
        db.session.commit()
        logger.info(f"Password reset token created for user ID: {user_id}")

    def get_password_reset_by_token(self, token: str) -> PasswordReset:
        return PasswordReset.query.filter_by(token=token).first()

    def delete_password_reset(self, password_reset: PasswordReset) -> None:
        db.session.delete(password_reset)
        db.session.commit()
        logger.info(f"Password reset token deleted for user ID: {password_reset.user_id}")