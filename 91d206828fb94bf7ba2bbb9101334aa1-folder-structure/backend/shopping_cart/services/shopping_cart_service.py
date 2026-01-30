# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def remove_from_cart(self, user_id: int, product_id: int) -> dict:
        if not self.shopping_cart_repository.exists_in_cart(user_id, product_id):
            return {"error": "Product not found in cart"}

        success = self.shopping_cart_repository.remove_cart_item(user_id, product_id)
        
        if success:
            return {"message": "Product removed from cart"}
        return {"error": "Failed to remove product from cart"}