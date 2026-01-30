# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        if not self.shopping_cart_repository.is_product_available(product_id):
            return {"error": "Product is not available"}

        cart_item_id = self.shopping_cart_repository.add_product_to_cart(user_id, product_id, quantity)
        if cart_item_id:
            return {"cart_item_id": cart_item_id, "message": "Product added to cart successfully"}
        return {"error": "Failed to add product to cart"}