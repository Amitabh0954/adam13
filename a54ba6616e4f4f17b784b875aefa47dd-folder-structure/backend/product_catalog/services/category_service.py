# Epic Title: Product Catalog Management
from repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None) -> dict:
        if not name:
            return {"error": "Category name cannot be empty"}

        category_id = self.category_repository.create_category(name, parent_id)
        return {"category_id": category_id, "message": "Category added successfully"}

    def assign_category(self, product_id: int, category_id: int) -> dict:
        if self.category_repository.assign_category(product_id, category_id):
            return {"message": "Category assigned to product successfully"}
        return {"error": "Failed to assign category"}