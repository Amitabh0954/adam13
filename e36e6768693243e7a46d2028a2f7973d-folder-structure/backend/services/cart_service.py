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

    def remove_from_cart(self, user_id: int, product_id: int) -> Dict[str, str]:
        if user_id:
            cart = self.cart_repository.get_cart_by_user(user_id)
        else:
            cart = self.cart_repository.get_cart_by_session()

        if not cart:
            return {'status': 'error', 'message': 'Cart not found'}

        self.cart_repository.remove_product_from_cart(cart, product_id)
        return {'status': 'success', 'message': 'Product removed from cart successfully'}

    def update_quantity(self, user_id: int, product_id: int, quantity: int) -> Dict[str, str]:
        if user_id:
            cart = self.cart_repository.get_cart_by_user(user_id)
        else:
            cart = self.cart_repository.get_cart_by_session()

        if not cart:
            return {'status': 'error', 'message': 'Cart not found'}

        if quantity <= 0:
            return {'status': 'error', 'message': 'Quantity must be a positive integer'}

        self.cart_repository.update_product_quantity(cart, product_id, quantity)
        return {'status': 'success', 'message': 'Product quantity updated successfully'}

    def save_cart(self, user_id: int) -> Dict[str, str]:
        if not self.cart_repository.get_cart_by_user(user_id):
            return {'status': 'error', 'message': 'No cart to save'}

        self.cart_repository.save_cart(user_id)
        return {'status': 'success', 'message': 'Cart saved successfully'}

    def load_cart(self, user_id: int) -> Dict:
        cart = self.cart_repository.load_cart(user_id)
        if not cart:
            return {'status': 'error', 'message': 'No saved cart found'}
        
        return {
            'status': 'success',
            'cart': cart.to_dict()
        }