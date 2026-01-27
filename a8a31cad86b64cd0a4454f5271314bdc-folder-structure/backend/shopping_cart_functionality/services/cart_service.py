# Epic Title: Shopping Cart Functionality

from backend.shopping_cart_functionality.repositories.cart_repository import CartRepository
from typing import Dict, Optional

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_to_cart(self, user_id: Optional[int], product_id: int, quantity: int) -> Dict[str, str]:
        if quantity <= 0:
            return {'status': 'error', 'message': 'Quantity must be a positive number'}

        self.cart_repository.add_to_cart(user_id, product_id, quantity)
        return {'status': 'success', 'message': 'Product added to cart'}

    def remove_from_cart(self, user_id: Optional[int], product_id: int) -> Dict[str, str]:
        self.cart_repository.remove_from_cart(user_id, product_id)
        return {'status': 'success', 'message': 'Product removed from cart'}

    def update_cart(self, user_id: Optional[int], product_id: int, quantity: int) -> Dict[str, str]:
        self.cart_repository.update_cart(user_id, product_id, quantity)
        return {'status': 'success', 'message': 'Cart updated successfully'}

    def get_cart(self, user_id: int) -> Dict:
        cart_items = self.cart_repository.get_cart_by_user(user_id)
        return {
            'total_items': len(cart_items),
            'products': [{
                'product_id': item.product_id,
                'quantity': item.quantity
            } for item in cart_items]
        }