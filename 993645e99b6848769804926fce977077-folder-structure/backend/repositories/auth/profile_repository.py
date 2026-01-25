import logging
from backend.models.user import User
from backend.database import db

logger = logging.getLogger(__name__)

class ProfileRepository:

    def get_user_by_id(self, user_id: int) -> User:
        return User.query.filter_by(id=user_id).first()
    
    def update_user(self, user: User) -> None:
        db.session.commit()
        logger.info(f"Profile updated for user: {user.email}")