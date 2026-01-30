# Epic Title: Product Catalog Management
from repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None) -> dict:
        if self.category_repository.exists_by_name(name):
            return {"error": "Category with this name already exists"}
        category_id = self.category_repository.create_category(name, parent_id)
        if category_id:
            return {"category_id": category_id, "message": "Category added successfully"}
        return {"error": "Failed to add category"}

    def get_categories(self) -> dict:
        categories = self.category_repository.get_all_categories()
        return {"categories": categories}

    def delete_category(self, category_id: int) -> dict:
        if not self.category_repository.exists_by_id(category_id):
            return {"error": "Category not found"}
        success = self.category_repository.delete_category(category_id)
        if success:
            return {"message": "Category deleted successfully"}
        return {"error": "Failed to delete category"}