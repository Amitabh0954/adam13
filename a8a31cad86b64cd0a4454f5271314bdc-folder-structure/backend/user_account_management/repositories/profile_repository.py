# Epic Title: User Account Management

from backend.database import db_session
from backend.user_account_management.models.profile import Profile

class ProfileRepository:
    def update_profile(self, user_id: int, data: dict):
        profile = db_session.query(Profile).filter_by(user_id=user_id).first()
        if not profile:
            profile = Profile(user_id=user_id)

        for key, value in data.items():
            setattr(profile, key, value)

        db_session.add(profile)
        db_session.commit()