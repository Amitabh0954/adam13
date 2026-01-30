# Epic Title: Product Categorization

from backend.products.repositories.category_repository import CategoryRepository
from backend.products.models.category import Category
from typing import List
import logging

logger = logging.getLogger(__name__)

class CategoryService:
    def __init__(self, category_repository: CategoryRepository) -> None:
        self.category_repository = category_repository

    def create_category(self, name: str, parent_name: str = None) -> Category:
        parent = None
        if parent_name:
            parent = self.category_repository.get_category_by_name(parent_name)
            if not parent:
                raise ValueError("Parent category not found")
        
        category = self.category_repository.add_category(name, parent)
        logger.info(f"Category {name} added with parent {parent_name}")
        return category

    def get_category(self, name: str) -> Category:
        category = self.category_repository.get_category_by_name(name)
        if not category:
            raise ValueError("Category not found")
        
        logger.info(f"Category retrieved: {category.name}")
        return category

    def list_categories(self) -> List[Category]:
        categories = self.category_repository.list_all_categories()
        logger.info("Retrieved all categories")
        return categories

    def delete_category(self, name: str) -> None:
        self.category_repository.delete_category(name)
        logger.info(f"Category {name} deleted")