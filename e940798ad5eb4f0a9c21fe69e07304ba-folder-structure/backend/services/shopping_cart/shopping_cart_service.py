# Epic Title: Shopping Cart Functionality
from backend.repositories.shopping_cart_repository import ShoppingCartRepository
from backend.models.shopping_cart.cart_item import CartItem

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        if not CartItem.validate_quantity(quantity):
            return {"error": "Quantity must be a positive number"}

        cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
        success = self.shopping_cart_repository.add_to_cart(cart_item)
        if not success:
            return {"error": "Failed to add product to cart"}

        return {"message": "Product added to cart successfully"}

    def get_cart(self, user_id: int) -> list:
        return self.shopping_cart_repository.get_cart(user_id)

    def clear_cart(self, user_id: int) -> dict:
        success = self.shopping_cart_repository.clear_cart(user_id)
        if not success:
            return {"error": "Failed to clear cart"}

        return {"message": "Cart cleared successfully"}

    def remove_product_from_cart(self, user_id: int, product_id: int, confirmation: str) -> dict:
        if confirmation != "YES":
            return {"error": "Confirmation required for removing product"}

        success = self.shopping_cart_repository.remove_from_cart(user_id, product_id)
        if not success:
            return {"error": "Failed to remove product from cart"}

        return {"message": "Product removed from cart successfully"}