# Epic Title: Product Catalog Management

from typing import Optional, List, Dict
from backend.repositories.product_catalog.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def add_category(self, name: str, parent_id: Optional[int] = None) -> Optional[str]:
        if not name:
            return "Category name cannot be empty"
        
        self.category_repository.add_category(name, parent_id)
        return None

    def update_category(self, category_id: int, name: str, parent_id: Optional[int] = None) -> Optional[str]:
        if not name:
            return "Category name cannot be empty"
        
        self.category_repository.update_category(category_id, name, parent_id)
        return None

    def delete_category(self, category_id: int) -> None:
        self.category_repository.delete_category(category_id)

    def get_all_categories(self) -> List[Dict[str, str]]:
        return self.category_repository.find_all_categories()