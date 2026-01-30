# Epic Title: Save Shopping Cart for Logged-in Users

from backend.repositories.cart_repository import CartRepository
from typing import Tuple, Optional

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_product_to_cart(self, user_id: Optional[int], session_key: str, product_id: int, quantity: int = 1) -> Tuple[bool, str]:
        if user_id:
            cart = self.cart_repository.get_cart_by_user(user_id)
            if not cart:
                cart = Cart(user_id=user_id)
                cart.save()
        else:
            cart = self.cart_repository.get_cart_by_session_key(session_key)
            if not cart:
                cart = Cart(session_key=session_key)
                cart.save()

        self.cart_repository.add_item_to_cart(cart, product_id, quantity)
        return True, 'Product added to cart successfully'

    def remove_product_from_cart(self, user_id: Optional[int], session_key: str, product_id: int) -> Tuple[bool, str]:
        if user_id:
            cart = self.cart_repository.get_cart_by_user(user_id)
        else:
            cart = self.cart_repository.get_cart_by_session_key(session_key)

        if not cart:
            return False, 'Cart not found'
        
        removed = self.cart_repository.remove_item_from_cart(cart, product_id)
        if removed:
            return True, 'Product removed from cart successfully'
        else:
            return False, 'Product not found in cart'

    def update_product_quantity_in_cart(self, user_id: Optional[int], session_key: str, product_id: int, quantity: int) -> Tuple[bool, str]:
        if user_id:
            cart = self.cart_repository.get_cart_by_user(user_id)
        else:
            cart = self.cart_repository.get_cart_by_session_key(session_key)

        if not cart:
            return False, 'Cart not found'
        
        if quantity <= 0:
            return False, 'Quantity must be a positive integer'
        
        updated = self.cart_repository.update_item_quantity(cart, product_id, quantity)
        if updated:
            return True, 'Product quantity updated successfully'
        else:
            return False, 'Product not found in cart'

    def save_cart_state(self, user_id: int) -> bool:
        cart = self.cart_repository.get_cart_by_user(user_id)
        if not cart:
            return False
        
        self.cart_repository.save_cart_state(cart)
        return True

    def retrieve_cart_state(self, user_id: int) -> Optional[dict]:
        cart = self.cart_repository.retrieve_cart_state(user_id)
        if not cart:
            return None
        
        cart_items = cart.items.all()
        cart_data = {
            'user_id': cart.user_id if cart.user else None,
            'session_key': cart.session_key,
            'items': [
                {'product_id': item.product_id, 'quantity': item.quantity}
                for item in cart_items
            ]
        }
        return cart_data