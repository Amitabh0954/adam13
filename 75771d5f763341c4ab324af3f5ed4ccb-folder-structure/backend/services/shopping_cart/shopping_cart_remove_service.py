# Epic Title: Remove Product from Shopping Cart

from repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartRemoveService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def remove_from_cart(self, data: dict) -> dict:
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        self.shopping_cart_repository.remove_product(user_id, product_id)
        return {"msg": "Product removed from cart successfully"}