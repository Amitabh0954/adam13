import logging
from backend.models.user import User
from backend.database import db

logger = logging.getLogger(__name__)

class ProfileRepository:

    def get_profile(self, user_id: int) -> User:
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def update_profile(self, user_id: int, data: dict) -> User:
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")

        for key, value in data.items():
            setattr(user, key, value)

        db.session.commit()
        logger.info("User profile updated successfully")
        return user