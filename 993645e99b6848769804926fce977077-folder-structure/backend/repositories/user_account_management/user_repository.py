import logging
from backend.models.user import User
from backend.database import db

logger = logging.getLogger(__name__)

class UserRepository:
    
    def get_user_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()
    
    def save_user(self, user: User) -> None:
        db.session.add(user)
        db.session.commit()
        logger.info(f"User saved with email: {user.email}")