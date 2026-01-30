# Epic Title: Shopping Cart Functionality

class CartItem:
    def __init__(self, user_id: int, product_id: int, quantity: int):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    @staticmethod
    def validate_quantity(quantity: int) -> bool:
        return quantity > 0