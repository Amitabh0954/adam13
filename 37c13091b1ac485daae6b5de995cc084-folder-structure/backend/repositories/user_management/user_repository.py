from backend.models.user import User
from backend.extensions import db

class UserRepository:
    # Inline comment referencing the Epic Title
    # Epic Title: Shopping Cart Functionality

    def find_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()
    
    def save_user(self, user: User):
        db.session.add(user)
        db.session.commit()

    def update_user(self, user: User):
        db.session.commit()