from backend.models.user import User
from backend.extensions import db

class ProfileRepository:
    def find_by_id(self, user_id: int) -> User:
        return User.query.get(user_id)
    
    def update_user(self, user: User):
        db.session.commit()