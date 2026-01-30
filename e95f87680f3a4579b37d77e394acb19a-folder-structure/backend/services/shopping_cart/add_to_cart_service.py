# Epic Title: Shopping Cart Functionality
from backend.repositories.shopping_cart_repository import ShoppingCartRepository

class AddToCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            cart_id = self.shopping_cart_repository.create_cart(user_id)
        else:
            cart_id = cart['id']

        existing_items = self.shopping_cart_repository.get_cart_items(cart_id)
        for item in existing_items:
            if item['product_id'] == product_id:
                new_quantity = item['quantity'] + quantity
                self.shopping_cart_repository.update_cart_item(cart_id, product_id, new_quantity)
                return {"message": "Product quantity updated in cart"}

        self.shopping_cart_repository.add_cart_item(cart_id, product_id, quantity)
        return {"message": "Product added to cart"}