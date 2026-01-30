# Epic Title: Shopping Cart Functionality
from repositories.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.cart_repository = ShoppingCartRepository()

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        if not self.cart_repository.product_exists(product_id):
            return {"error": "Product does not exist"}

        cart_id = self.cart_repository.get_active_cart(user_id)
        if not cart_id:
            cart_id = self.cart_repository.create_cart(user_id)

        added_to_cart = self.cart_repository.add_product(cart_id, product_id, quantity)
        if added_to_cart:
            return {"message": "Product added to cart successfully"}
        return {"error": "Failed to add product to cart"}

    def remove_product_from_cart(self, user_id: int, product_id: int) -> dict:
        cart_id = self.cart_repository.get_active_cart(user_id)
        if not cart_id:
            return {"error": "No active cart found"}

        if not self.cart_repository.product_in_cart(cart_id, product_id):
            return {"error": "Product not found in cart"}

        removed = self.cart_repository.remove_product(cart_id, product_id)
        if removed:
            return {"message": "Product removed from cart successfully"}
        return {"error": "Failed to remove product from cart"}

    def update_product_quantity(self, user_id: int, product_id: int, quantity: int) -> dict:
        cart_id = self.cart_repository.get_active_cart(user_id)
        if not cart_id:
            return {"error": "No active cart found"}

        if not self.cart_repository.product_in_cart(cart_id, product_id):
            return {"error": "Product not found in cart"}

        updated = self.cart_repository.update_product_quantity(cart_id, product_id, quantity)
        if updated:
            return {"message": "Product quantity updated successfully"}
        return {"error": "Failed to update product quantity"}

    def save_cart(self, user_id: int) -> dict:
        cart_id = self.cart_repository.get_active_cart(user_id)
        if not cart_id:
            return {"error": "No active cart found"}

        saved = self.cart_repository.save_cart_state(user_id, cart_id)
        if saved:
            return {"message": "Cart saved successfully"}
        return {"error": "Failed to save cart"}