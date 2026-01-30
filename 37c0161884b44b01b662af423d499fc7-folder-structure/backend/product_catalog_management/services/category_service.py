# Epic Title: Product Categorization

from typing import Optional, List
from product_catalog_management.repositories.category_repository import CategoryRepository
from product_catalog_management.models.category import Category

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_name: Optional[str] = None) -> Optional<Category]:
        parent_category = None
        if parent_name:
            parent_category = self.category_repository.get_category_by_name(parent_name)
            if not parent_category:
                return None
        return self.category_repository.create_category(name, parent_category)

    def get_all_categories(self) -> List[Category]:
        return self.category_repository.get_all_categories()

    def delete_category(self, name: str) -> bool:
        category = self.category_repository.get_category_by_name(name)
        if category:
            self.category_repository.delete_category(category)
            return True
        return False