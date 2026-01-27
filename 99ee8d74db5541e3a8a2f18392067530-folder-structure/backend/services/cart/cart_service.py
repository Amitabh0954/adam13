# Epic Title: Shopping Cart Functionality

from backend.repositories.cart.cart_repository import CartRepository
from typing import Dict, Any

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_to_cart(self, session: Dict[str, Any], product_id: int, quantity: int):
        user_id = session.get('user_id')
        self.cart_repository.add_to_cart(user_id, product_id, quantity)

    def get_cart(self, session: Dict[str, Any]) -> Dict[str, Any]:
        user_id = session.get('user_id')
        if user_id:
            return self.cart_repository.get_cart(user_id)
        else:
            return session.get('cart', {})

    def remove_from_cart(self, session: Dict[str, Any], product_id: int):
        user_id = session.get('user_id')
        self.cart_repository.remove_from_cart(user_id, product_id)