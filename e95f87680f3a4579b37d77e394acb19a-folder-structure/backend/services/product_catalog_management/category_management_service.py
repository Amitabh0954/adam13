# Epic Title: Product Catalog Management
from backend.repositories.category_repository import CategoryRepository

class CategoryManagementService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def get_all_categories(self) -> list:
        return self.category_repository.get_all_categories()

    def create_category(self, name: str, parent_id: int = None) -> dict:
        self.category_repository.create_category(name, parent_id)
        return {"message": "Category created successfully"}

    def update_category(self, category_id: int, name: str, parent_id: int = None) -> dict:
        updated = self.category_repository.update_category(category_id, name, parent_id)
        if updated:
            return {"message": "Category updated successfully"}
        return {"error": "Failed to update category"}

    def delete_category(self, category_id: int) -> dict:
        deleted = self.category_repository.delete_category(category_id)
        if deleted:
            return {"message": "Category deleted successfully"}
        return {"error": "Failed to delete category"}