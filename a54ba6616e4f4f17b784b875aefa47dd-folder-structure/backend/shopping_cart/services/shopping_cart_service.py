# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()
        
    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        if not product_id:
            return {"error": "Product ID is required"}
        if quantity <= 0:
            return {"error": "Quantity must be greater than 0"}
        
        cart_item_id = self.shopping_cart_repository.add_to_cart(user_id, product_id, quantity)
        return {"cart_item_id": cart_item_id, "message": "Product added to cart successfully"}