# Epic Title: Update Product Details

class ProductUpdateValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_name()
        self.check_price()
        self.check_description()
        return len(self.errors) == 0

    def check_name(self):
        name = self.data.get('name', '')
        if not name:
            self.errors.append("Name is required.")
    
    def check_price(self):
        try:
            price = float(self.data.get('price', ''))
            if price <= 0:
                self.errors.append("Price must be a positive number.")
        except ValueError:
            self.errors.append("Price must be a valid number.")

    def check_description(self):
        description = self.data.get('description', '')
        if not description:
            self.errors.append("Description is required.")