from backend.repositories.product.category_repository import CategoryRepository

class CategoryService:

    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None):
        return self.category_repository.add_category(name, parent_id)

    def update_category(self, category_id: int, name: str = None, parent_id: int = None):
        return self.category_repository.update_category(category_id, name, parent_id)