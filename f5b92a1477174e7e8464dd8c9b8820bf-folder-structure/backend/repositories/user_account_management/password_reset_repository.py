import logging
from backend.models.password_reset import PasswordReset
from backend.models.user import User
from backend.database import db
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class PasswordResetRepository:
    
    def create_reset_token(self, email: str) -> PasswordReset:
        user = User.query.filter_by(email=email).first()
        if not user:
            raise ValueError("Email not found")
        
        reset_token = PasswordReset(user_id=user.id, token="random_generated_token", expiry=datetime.utcnow() + timedelta(hours=24))
        db.session.add(reset_token)
        db.session.commit()
        logger.info(f"Password reset token created for user: {email}")
        return reset_token
    
    def validate_reset_token(self, token: str) -> PasswordReset:
        reset = PasswordReset.query.filter_by(token=token).first()
        if not reset or reset.expiry < datetime.utcnow():
            raise ValueError("Invalid or expired token")
        return reset
    
    def update_password(self, user_id: int, new_password: str):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")
        
        user.password = new_password
        db.session.commit()
        logger.info("Password updated successfully")