# Epic Title: Shopping Cart Functionality

from typing import Optional, List, Dict
from backend.repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self.shopping_cart_repository = shopping_cart_repository

    def add_product_to_cart(self, user_id: Optional[int], product_id: int, quantity: int) -> Optional[str]:
        if quantity <= 0:
            return "Quantity must be a positive number"

        cart_id = self.shopping_cart_repository.create_cart(user_id)
        self.shopping_cart_repository.add_product_to_cart(cart_id, product_id, quantity)
        return None

    def get_cart_items(self, user_id: Optional[int]) -> List[Dict[str, int]]:
        cart_id = self.shopping_cart_repository.create_cart(user_id)
        return self.shopping_cart_repository.get_cart_items(cart_id)

    def remove_product_from_cart(self, user_id: Optional[int], product_id: int, confirmation: str) -> Optional[str]:
        if confirmation != 'yes':
            return "Product removal not confirmed"

        cart_id = self.shopping_cart_repository.create_cart(user_id)
        self.shopping_cart_repository.remove_product_from_cart(cart_id, product_id)
        return None