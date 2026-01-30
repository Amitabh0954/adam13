# Epic Title: Product Categorization

from catalog.repositories.category_repository import CategoryRepository
from catalog.models.category import Category
from typing import Optional, List

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_category: Optional[Category] = None) -> Category:
        return self.category_repository.create_category(name, parent_category)

    def get_category_by_name(self, name: str) -> Optional<Category]:
        return self.category_repository.get_category_by_name(name)

    def get_all_categories(self) -> List[Category]:
        return self.category_repository.get_all_categories()