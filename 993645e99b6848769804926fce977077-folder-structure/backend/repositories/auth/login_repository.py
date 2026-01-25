import logging
from backend.models.user import User
from backend.database import db

logger = logging.getLogger(__name__)

class LoginRepository:
    
    def get_user_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def update_login_attempts(self, user: User) -> None:
        user.login_attempts += 1
        db.session.commit()
        logger.info(f"Updated login attempts for user: {user.email}")

    def reset_login_attempts(self, user: User) -> None:
        user.login_attempts = 0
        db.session.commit()
        logger.info(f"Reset login attempts for user: {user.email}")