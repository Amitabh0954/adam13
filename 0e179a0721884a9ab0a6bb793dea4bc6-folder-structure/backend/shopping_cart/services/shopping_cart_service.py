# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def remove_product_from_cart(self, user_id: int, cart_item_id: int) -> dict:
        success = self.shopping_cart_repository.remove_product_from_cart(user_id, cart_item_id)
        if success:
            return {"message": "Product removed from cart successfully"}
        return {"error": "Failed to remove product from cart"}