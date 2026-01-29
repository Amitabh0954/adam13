# Epic Title: Modify Quantity of Products in Shopping Cart

from repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository

class ShoppingCartModifyService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def modify_cart_quantity(self, data: dict) -> dict:
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        self.shopping_cart_repository.update_quantity(user_id, product_id, quantity)
        return {"msg": "Cart quantity updated successfully"}