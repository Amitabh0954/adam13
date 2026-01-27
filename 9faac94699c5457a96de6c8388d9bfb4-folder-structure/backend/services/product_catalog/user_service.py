# Epic Title: Shopping Cart Functionality

from flask import session
from backend.repositories.user_account.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def is_user_logged_in(self) -> bool:
        return 'user_id' in session

    def get_current_user_id(self) -> int:
        return session.get('user_id')

    def get_user_cart(self, user_id: int) -> dict:
        user = self.user_repository.get_user_by_id(user_id)
        return user.cart if user and user.cart else {}

    def save_user_cart(self, user_id: int, cart: dict):
        self.user_repository.update_user_cart(user_id, cart)
        session[f'cart_{user_id}'] = cart