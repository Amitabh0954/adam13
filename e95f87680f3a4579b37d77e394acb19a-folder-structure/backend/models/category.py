# Epic Title: Product Catalog Management

class Category:
    def __init__(self, id: int, name: str, parent_id: int = None):
        self.id = id
        self.name = name
        self.parent_id = parent_id