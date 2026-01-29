# Epic Title: Shopping Cart Functionality

from typing import Optional
from structured_logging import get_logger
from backend.shopping_cart_functionality.repositories.cart_repository import CartRepository
from backend.shopping_cart_functionality.models.cart import Cart

logger = get_logger(__name__)

class CartService:
    
    def __init__(self, cart_repository: CartRepository) -> None:
        self.cart_repository = cart_repository
    
    def add_product_to_cart(self, user_id: Optional[int], session_id: Optional[str], product_id: int, quantity: int) -> bool:
        if user_id:
            cart = self.cart_repository.find_cart_by_user_id(user_id)
            if not cart:
                cart = self.cart_repository.create_cart_for_user(user_id)
        elif session_id:
            cart = self.cart_repository.find_cart_by_session_id(session_id)
            if not cart:
                cart = self.cart_repository.create_cart_for_session(session_id)
        else:
            logger.error("User ID or Session ID must be provided")
            return False
        
        self.cart_repository.add_item_to_cart(cart, product_id, quantity)
        logger.info("Product added to cart successfully")
        return True
    
    def remove_product_from_cart(self, user_id: Optional[int], session_id: Optional[str], product_id: int) -> bool:
        if user_id:
            cart = self.cart_repository.find_cart_by_user_id(user_id)
        elif session_id:
            cart = self.cart_repository.find_cart_by_session_id(session_id)
        else:
            logger.error("User ID or Session ID must be provided")
            return False
        
        if not cart:
            logger.error("Cart not found")
            return False
        
        self.cart_repository.remove_item_from_cart(cart, product_id)
        logger.info("Product removed from cart successfully")
        return True