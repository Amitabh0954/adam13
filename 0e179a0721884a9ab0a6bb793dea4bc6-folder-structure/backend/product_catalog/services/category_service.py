# Epic Title: Product Catalog Management
from repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int | None) -> dict:
        if parent_id and not self.category_repository.exists(parent_id):
            return {"error": "Parent category does not exist"}
        
        category_id = self.category_repository.create_category(name, parent_id)
        if category_id:
            return {"category_id": category_id, "message": "Category added successfully"}
        return {"error": "Failed to add category"}

    def delete_category(self, category_id: int) -> dict:
        success = self.category_repository.delete_category(category_id)
        if success:
            return {"message": "Category deleted successfully"}
        return {"error": "Failed to delete category"}

    def get_all_categories(self) -> list:
        return self.category_repository.get_all_categories()