# Epic Title: Shopping Cart Functionality

from flask import session

class UserService:
    def is_user_logged_in(self) -> bool:
        return 'user_id' in session

    def get_current_user_id(self) -> int:
        return session.get('user_id')

    def get_user_cart(self, user_id: int) -> dict:
        # This should fetch the cart from a database in a real application
        return session.get(f'cart_{user_id}', {})

    def save_user_cart(self, user_id: int, cart: dict):
        # This should save the cart to a database in a real application
        session[f'cart_{user_id}'] = cart