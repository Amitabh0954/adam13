import logging
from backend.models.user import User
from backend.database import db

logger = logging.getLogger(__name__)

class UserRepository:
    
    def get_user_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def create_user(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        logger.info(f"User created with email: {email}")
        return user
    
    def verify_password(self, user: User, password: str) -> bool:
        return user.password == password