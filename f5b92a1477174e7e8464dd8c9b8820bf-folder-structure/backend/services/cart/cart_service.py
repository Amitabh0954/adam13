from backend.repositories.cart.cart_repository import CartRepository

class CartService:

    def __init__(self):
        self.cart_repository = CartRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        return self.cart_repository.add_to_cart(user_id, product_id, quantity)

    def get_cart(self, user_id: int):
        return self.cart_repository.get_cart(user_id)

    def remove_from_cart(self, user_id: int, cart_item_id: int):
        return self.cart_repository.remove_from_cart(user_id, cart_item_id)