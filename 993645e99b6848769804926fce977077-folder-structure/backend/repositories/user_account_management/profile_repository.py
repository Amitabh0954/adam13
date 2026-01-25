import logging
from backend.models.profile import Profile
from backend.database import db

logger = logging.getLogger(__name__)

class ProfileRepository:
    
    def get_profile_by_user_id(self, user_id: int) -> Profile:
        return Profile.query.filter_by(user_id=user_id).first()
    
    def save_profile(self, profile: Profile) -> None:
        db.session.add(profile)
        db.session.commit()
        logger.info(f"Profile saved for user {profile.user_id}")