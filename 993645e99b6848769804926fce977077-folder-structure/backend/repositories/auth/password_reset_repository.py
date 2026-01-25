import logging
from backend.models.password_reset_token import PasswordResetToken
from backend.models.user import User
from backend.database import db
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class PasswordResetRepository:
    
    def create_password_reset_token(self, user: User) -> PasswordResetToken:
        token = PasswordResetToken(user_id=user.id)
        db.session.add(token)
        db.session.commit()
        logger.info(f"Created password reset token for user: {user.email}")
        return token

    def get_user_by_reset_token(self, token: str) -> User:
        reset_token = PasswordResetToken.query.filter_by(token=token).first()
        if not reset_token or reset_token.expiration < datetime.utcnow():
            raise ValueError("Invalid or expired password reset token")
        
        return User.query.filter_by(id=reset_token.user_id).first()

    def delete_password_reset_token(self, token: str) -> None:
        reset_token = PasswordResetToken.query.filter_by(token=token).first()
        if reset_token:
            db.session.delete(reset_token)
            db.session.commit()
            logger.info(f"Deleted password reset token: {token}")