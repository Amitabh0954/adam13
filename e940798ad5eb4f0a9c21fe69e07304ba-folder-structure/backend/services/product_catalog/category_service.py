# Epic Title: Product Catalog Management
from backend.repositories.category_repository import CategoryRepository
from backend.models.product_catalog.category import Category

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, description: str, parent_id: int = None) -> dict:
        if not Category.validate_name(name):
            return {"error": "Category name cannot be empty"}
        if not Category.validate_description(description):
            return {"error": "Category description cannot be empty"}

        existing_category = self.category_repository.get_category_by_name(name)
        if existing_category:
            return {"error": "Category with the same name already exists"}

        category = Category(id=None, name=name, description=description, parent_id=parent_id)
        success = self.category_repository.add_category(category)
        if not success:
            return {"error": "Failed to add category"}

        return {"message": "Category added successfully"}

    def get_all_categories(self) -> list:
        return self.category_repository.get_all_categories()