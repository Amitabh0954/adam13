# Epic Title: Shopping Cart Functionality
from backend.repositories.shopping_cart_repository import ShoppingCartRepository

class RemoveFromCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def remove_from_cart(self, user_id: int, product_id: int) -> dict:
        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            return {"error": "Shopping cart not found"}

        cart_id = cart['id']
        deleted = self.shopping_cart_repository.delete_cart_item(cart_id, product_id)
        if deleted:
            return {"message": "Product removed from cart"}
        return {"error": "Failed to remove product from cart"}