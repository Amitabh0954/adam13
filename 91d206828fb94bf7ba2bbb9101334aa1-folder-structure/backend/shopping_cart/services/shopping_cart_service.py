# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        cart_item = self.shopping_cart_repository.get_cart_item(user_id, product_id)
        
        if cart_item:
            self.shopping_cart_repository.update_cart_item(user_id, product_id, cart_item['quantity'] + quantity)
            return {"message": "Product quantity updated in cart"}
        
        cart_item_id = self.shopping_cart_repository.add_cart_item(user_id, product_id, quantity)
        if cart_item_id:
            return {"cart_item_id": cart_item_id, "message": "Product added to cart"}
        
        return {"error": "Failed to add product to cart"}