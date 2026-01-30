# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()
        
    def modify_quantity(self, user_id: int, product_id: int, quantity: int) -> dict:
        if not product_id:
            return {"error": "Product ID is required"}
        if quantity <= 0:
            return {"error": "Quantity must be a positive integer"}

        if self.shopping_cart_repository.modify_quantity(user_id, product_id, quantity):
            return {"message": "Product quantity updated successfully"}
        return {"error": "Failed to update product quantity"}