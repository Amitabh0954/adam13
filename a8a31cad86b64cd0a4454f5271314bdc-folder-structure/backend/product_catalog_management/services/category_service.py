# Epic Title: Product Catalog Management

from backend.product_catalog_management.repositories.category_repository import CategoryRepository
from typing import Dict

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None) -> Dict[str, str]:
        if self.category_repository.get_category_by_name(name):
            return {'status': 'error', 'message': 'Category name already exists'}

        self.category_repository.add_category(name, parent_id)
        return {'status': 'success', 'message': 'Category added successfully'}

    def update_category(self, category_id: int, name: str, parent_id: int = None) -> Dict[str, str]:
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            return {'status': 'error', 'message': 'Category not found'}

        category.name = name
        category.parent_id = parent_id

        self.category_repository.update_category(category)
        return {'status': 'success', 'message': 'Category updated successfully'}

    def delete_category(self, category_id: int) -> Dict[str, str]:
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            return {'status': 'error', 'message': 'Category not found'}

        self.category_repository.delete_category(category)
        return {'status': 'success', 'message': 'Category deleted successfully'}