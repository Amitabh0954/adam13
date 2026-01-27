# Epic Title: Product Catalog Management

from backend.repositories.product_catalog.category_repository import CategoryRepository
from typing import List, Dict

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None) -> dict:
        if parent_id and not self.category_repository.get_category_by_id(parent_id):
            return {'status': 'error', 'message': 'Parent category not found'}

        self.category_repository.create_category(name, parent_id)
        return {'status': 'success', 'message': 'Category added successfully'}

    def get_categories(self) -> List[Dict]:
        categories = self.category_repository.get_all_categories()
        return [category.to_dict() for category in categories]