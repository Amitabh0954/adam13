from backend.models.user import User
from backend.extensions import db

class UserRepository:
    def find_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()
    
    def find_by_id(self, user_id: int) -> User:
        return User.query.get(user_id)
    
    def save_user(self, user: User):
        db.session.add(user)
        db.session.commit()