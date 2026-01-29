# Epic Title: Save Shopping Cart for Logged-in Users

from repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartSaveService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def save_cart(self, data: dict) -> dict:
        user_id = data.get('user_id')
        cart_items = data.get('cart_items', [])
        self.shopping_cart_repository.save_cart(user_id, cart_items)
        return {"msg": "Shopping cart saved successfully"}

    def load_cart(self, user_id: int) -> dict:
        cart_items = self.shopping_cart_repository.load_cart(user_id)
        return {"cart_items": cart_items}