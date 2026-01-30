# Epic Title: Shopping Cart Functionality
from backend.repositories.shopping_cart_repository import ShoppingCartRepository

class UpdateCartItemService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def update_cart_item(self, user_id: int, product_id: int, quantity: int) -> dict:
        if quantity < 1:
            return {"error": "Quantity must be a positive integer"}

        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            return {"error": "Shopping cart not found"}

        cart_id = cart['id']
        updated = self.shopping_cart_repository.update_cart_item(cart_id, product_id, quantity)
        if updated:
            return {"message": "Product quantity updated in cart"}
        return {"error": "Failed to update product quantity in cart"}