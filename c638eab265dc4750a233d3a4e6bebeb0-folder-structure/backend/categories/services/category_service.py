# Epic Title: Product Categorization

from categories.repositories.category_repository import CategoryRepository
from categories.models.category import Category
from typing import Optional, List

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: Optional[int]) -> Optional<Category]:
        parent = None
        if parent_id:
            parent = self.category_repository.get_category_by_id(parent_id)
        if self.category_repository.get_category_by_name(name):
            return None
        return self.category_repository.add_category(name, parent)

    def get_all_categories(self) -> List[Category]:
        return self.category_repository.get_all_categories()

    def delete_category(self, category_id: int) -> bool:
        return self.category_repository.delete_category_by_id(category_id)