# Epic Title: Product Catalog Management
from repositories.category_repository import CategoryRepository

class CategoryManagementService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def get_all_categories(self) -> list:
        return self.category_repository.fetch_all_categories()

    def create_category(self, data: dict) -> dict:
        name = data.get('name')
        parent_id = data.get('parent_id')

        if not name:
            return {"error": "Category name is required"}

        category_id = self.category_repository.create_category(name, parent_id)
        return {"category_id": category_id, "message": "Category created successfully"}
    
    def update_category(self, category_id: int, data: dict) -> dict:
        name = data.get('name')
        parent_id = data.get('parent_id')

        if not name:
            return {"error": "Category name is required"}

        updated = self.category_repository.update_category(category_id, name, parent_id)
        if updated:
            return {"message": "Category updated successfully"}
        
        return {"error": "Category update failed"}