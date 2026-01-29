# Epic Title: User Account Management

from typing import Optional
from sqlalchemy.orm import Session
from backend.user_account_management.models.profile import Profile

class ProfileRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_profile(self, profile: Profile) -> None:
        self.session.add(profile)
        self.session.commit()
    
    def find_by_user_id(self, user_id: int) -> Optional[Profile]:
        return self.session.query(Profile).filter_by(user_id=user_id).first()
    
    def update_profile(self, profile: Profile) -> None:
        existing_profile = self.find_by_user_id(profile.user_id)
        if existing_profile:
            existing_profile.first_name = profile.first_name
            existing_profile.last_name = profile.last_name
            existing_profile.preferences = profile.preferences
            self.session.commit()