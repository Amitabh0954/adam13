# Epic Title: Add Product to Shopping Cart

from repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_to_cart(self, data: dict) -> dict:
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        cart_id = self.shopping_cart_repository.add_product(user_id, product_id, quantity)
        return {"msg": "Product added to cart successfully", "cart_id": cart_id}