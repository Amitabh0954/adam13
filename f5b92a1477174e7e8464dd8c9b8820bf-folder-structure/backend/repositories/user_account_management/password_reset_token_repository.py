import logging
from backend.models.password_reset_token import PasswordResetToken
from backend.database import db
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class PasswordResetTokenRepository:

    def create_token(self, user_id: int) -> PasswordResetToken:
        token = PasswordResetToken(user_id=user_id, expires_at=datetime.utcnow() + timedelta(hours=24))
        db.session.add(token)
        db.session.commit()
        logger.info(f"Password reset token created for user {user_id}")
        return token

    def get_token(self, token: str) -> PasswordResetToken:
        return PasswordResetToken.query.filter_by(token=token).first()
    
    def delete_token(self, token: PasswordResetToken) -> None:
        db.session.delete(token)
        db.session.commit()
        logger.info(f"Password reset token {token.token} deleted")