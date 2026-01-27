# Epic Title: Product Catalog Management

from backend.repositories.product.category_repository import CategoryRepository
from typing import Dict, Optional

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: Optional[int]) -> Dict[str, str]:
        if self.category_repository.get_category_by_name(name):
            return {'status': 'error', 'message': 'Category name must be unique'}

        self.category_repository.add_category(name, parent_id)
        return {'status': 'success', 'message': 'Category added successfully'}

    def update_category(self, category_id: int, name: Optional[str], parent_id: Optional[int]) -> Dict[str, str]:
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            return {'status': 'error', 'message': 'Category not found'}

        if name:
            if self.category_repository.get_category_by_name(name):
                return {'status': 'error', 'message': 'Category name must be unique'}
            category.name = name
        if parent_id:
            category.parent_id = parent_id

        self.category_repository.update_category(category)
        return {'status': 'success', 'message': 'Category updated successfully'}

    def delete_category(self, category_id: int) -> Dict[str, str]:
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            return {'status': 'error', 'message': 'Category not found'}

        self.category_repository.delete_category(category)
        return {'status': 'success', 'message': 'Category deleted successfully'}