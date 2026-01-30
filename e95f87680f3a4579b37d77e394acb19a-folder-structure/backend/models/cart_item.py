# Epic Title: Shopping Cart Functionality

class CartItem:
    def __init__(self, cart_id: int, product_id: int, quantity: int):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity