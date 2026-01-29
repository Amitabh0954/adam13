# Epic Title: Modify Quantity of Products in Shopping Cart

class ShoppingCartModifyValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_user_id()
        self.check_product_id()
        self.check_quantity()
        return len(self.errors) == 0
    
    def check_user_id(self):
        user_id = self.data.get('user_id')
        if user_id is not None and not isinstance(user_id, int):
            self.errors.append("User ID, if provided, must be an integer.")
    
    def check_product_id(self):
        product_id = self.data.get('product_id')
        if product_id is None:
            self.errors.append("Product ID is required.")
        elif not isinstance(product_id, int):
            self.errors.append("Product ID must be an integer.")
    
    def check_quantity(self):
        quantity = self.data.get('quantity')
        if quantity is None:
            self.errors.append("Quantity is required.")
        elif not isinstance(quantity, int) or quantity <= 0:
            self.errors.append("Quantity must be a positive integer.")