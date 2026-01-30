# Epic Title: Product Categorization

from backend.repositories.category_repository import CategoryRepository
from typing import Tuple, Optional, List

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: Optional[int] = None) -> Tuple[bool, str]:
        if self.category_repository.get_category_by_name(name):
            return False, 'Category name must be unique'
        
        self.category_repository.add_category(name, parent_id)
        return True, 'Category added successfully'

    def get_all_categories(self) -> Optional[List[dict]]:
        categories = self.category_repository.get_all_categories()
        if not categories:
            return None
        
        categories_data = [
            {
                'name': category.name,
                'parent': category.parent.name if category.parent else None,
            }
            for category in categories
        ]
        return categories_data