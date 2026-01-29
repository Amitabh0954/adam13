# Epic Title: Search Products

class ProductSearchValidator:
    def __init__(self, params: dict):
        self.params = params
        self.errors = []
    
    def is_valid(self) -> bool:
        self.errors = []
        self.check_query()
        self.check_page()
        self.check_limit()
        return len(self.errors) == 0

    def check_query(self):
        query = self.params.get('query', '')
        if not query:
            self.errors.append("Query parameter is required.")
    
    def check_page(self):
        try:
            page = int(self.params.get('page', '1'))
            if page <= 0:
                self.errors.append("Page must be a positive integer.")
        except ValueError:
            self.errors.append("Page must be a valid integer.")
    
    def check_limit(self):
        try:
            limit = int(self.params.get('limit', '10'))
            if limit <= 0:
                self.errors.append("Limit must be a positive integer.")
        except ValueError:
            self.errors.append("Limit must be a valid integer.")