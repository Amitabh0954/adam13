# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def modify_quantity(self, user_id: int, cart_item_id: int, quantity: int) -> dict:
        success = self.shopping_cart_repository.modify_quantity(user_id, cart_item_id, quantity)
        if success:
            return {"message": "Product quantity updated successfully"}
        return {"error": "Failed to update product quantity"}