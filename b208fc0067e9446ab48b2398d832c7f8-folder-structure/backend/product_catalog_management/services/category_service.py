# Epic Title: Product Categorization

from product_catalog_management.repositories.category_repository import CategoryRepository
from product_catalog_management.models.category import Category
from typing import Optional

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def create_category(self, name: str, parent_category_name: Optional[str] = None) -> Optional[Category]:
        parent_category = None
        if parent_category_name:
            parent_category = self.category_repository.get_category_by_name(parent_category_name)
        return self.category_repository.create_category(name, parent_category)