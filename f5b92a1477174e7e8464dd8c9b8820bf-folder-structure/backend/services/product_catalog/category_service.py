from backend.repositories.product.category_repository import CategoryRepository

class CategoryService:
    
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None):
        return self.category_repository.add_category(name, parent_id)

    def get_all_categories(self):
        return self.category_repository.get_all_categories()