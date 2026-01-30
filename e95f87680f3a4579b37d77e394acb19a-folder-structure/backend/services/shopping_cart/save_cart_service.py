# Epic Title: Shopping Cart Functionality
from backend.repositories.shopping_cart_repository import ShoppingCartRepository

class SaveCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def save_cart_state(self, user_id: int, cart_items: list) -> dict:
        saved = self.shopping_cart_repository.save_cart_state(user_id, cart_items)
        if saved:
            return {"message": "Shopping cart state saved"}
        return {"error": "Failed to save shopping cart state"}

    def retrieve_cart_state(self, user_id: int) -> list:
        return self.shopping_cart_repository.retrieve_cart_state(user_id)