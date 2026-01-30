# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def save_cart(self, user_id: int) -> dict:
        saved = self.shopping_cart_repository.save_cart_state(user_id)
        
        if saved:
            return {"message": "Cart state saved successfully"}
        return {"error": "Failed to save cart state"}