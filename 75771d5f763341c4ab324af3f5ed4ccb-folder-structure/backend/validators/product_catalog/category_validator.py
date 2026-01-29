# Epic Title: Product Categorization

class CategoryValidator:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_name()
        return len(self.errors) == 0

    def check_name(self):
        name = self.data.get('name', '')
        if not name:
            self.errors.append("Name is required.")