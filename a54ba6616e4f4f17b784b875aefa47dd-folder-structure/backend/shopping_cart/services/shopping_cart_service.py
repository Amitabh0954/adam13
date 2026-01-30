# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()
        
    def remove_from_cart(self, user_id: int, product_id: int) -> dict:
        if not product_id:
            return {"error": "Product ID is required"}
        
        if self.shopping_cart_repository.remove_from_cart(user_id, product_id):
            return {"message": "Product removed from cart successfully"}
        return {"error": "Failed to remove product from cart"}