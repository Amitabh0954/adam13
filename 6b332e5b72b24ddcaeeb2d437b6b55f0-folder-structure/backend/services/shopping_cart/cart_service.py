# Epic Title: Modify Quantity of Products in Shopping Cart

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