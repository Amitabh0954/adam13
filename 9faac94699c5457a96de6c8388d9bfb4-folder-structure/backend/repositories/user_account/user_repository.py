# Epic Title: Shopping Cart Functionality

from backend.database import db_session
from backend.models.user import User

class UserRepository:
    def get_user_by_id(self, user_id: int) -> User:
        return db_session.query(User).filter_by(id=user_id).first()

    def update_user_cart(self, user_id: int, cart: dict):
        user = self.get_user_by_id(user_id)
        if user:
            user.cart = cart
            db_session.add(user)
            db_session.commit()