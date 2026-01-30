# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()
        
    def save_cart(self, user_id: int) -> dict:
        if self.shopping_cart_repository.save_cart(user_id):
            return {"message": "Shopping cart saved successfully"}
        return {"error": "Failed to save shopping cart"}

    def retrieve_cart(self, user_id: int) -> dict:
        cart_items = self.shopping_cart_repository.retrieve_cart(user_id)
        
        if cart_items is not None:
            return {"cart_items": cart_items}
        return {"error": "Failed to retrieve shopping cart"}