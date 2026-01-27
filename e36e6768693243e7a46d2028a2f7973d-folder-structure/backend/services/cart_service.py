# Epic Title: Shopping Cart Functionality

from backend.repositories.cart_repository import CartRepository
from typing import Dict

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> Dict[str, str]:
        if user_id:
            cart = self.cart_repository.get_cart_by_user(user_id)
        else:
            cart = self.cart_repository.get_cart_by_session()

        if not cart:
            cart = self.cart_repository.create_cart(user_id)

        self.cart_repository.add_product_to_cart(cart, product_id, quantity)
        return {'status': 'success', 'message': 'Product added to cart successfully'}