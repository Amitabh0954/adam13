# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def modify_cart_quantity(self, user_id: int, product_id: int, quantity: int) -> dict:
        if not self.shopping_cart_repository.exists_in_cart(user_id, product_id):
            return {"error": "Product not found in cart"}

        success = self.shopping_cart_repository.update_cart_item(user_id, product_id, quantity)
        
        if success:
            return {"message": "Product quantity updated in cart"}
        return {"error": "Failed to update product quantity in cart"}