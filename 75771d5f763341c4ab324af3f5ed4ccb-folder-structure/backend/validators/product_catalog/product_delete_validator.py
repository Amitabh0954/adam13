# Epic Title: Delete Product

class ProductDeleteValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_confirmation()
        return len(self.errors) == 0
    
    def check_confirmation(self):
        confirmation = self.data.get('confirmation', False)
        if not confirmation:
            self.errors.append("Deletion requires confirmation.")