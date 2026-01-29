# Epic Title: Save Shopping Cart for Logged-in Users

class ShoppingCartSaveValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_user_id()
        self.check_cart_items()
        return len(self.errors) == 0
    
    def check_user_id(self):
        user_id = self.data.get('user_id')
        if user_id is None:
            self.errors.append("User ID is required.")
        elif not isinstance(user_id, int):
            self.errors.append("User ID must be an integer.")
    
    def check_cart_items(self):
        cart_items = self.data.get('cart_items', [])
        if not isinstance(cart_items, list):
            self.errors.append("Cart items must be a list.")