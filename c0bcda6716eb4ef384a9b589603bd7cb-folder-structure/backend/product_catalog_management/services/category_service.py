# Epic Title: Product Catalog Management

from typing import Optional, List, Dict
from structured_logging import get_logger
from backend.product_catalog_management.repositories.category_repository import CategoryRepository
from backend.product_catalog_management.models.category import Category

logger = get_logger(__name__)

class CategoryService:
    
    def __init__(self, category_repository: CategoryRepository) -> None:
        self.category_repository = category_repository
    
    def add_category(self, name: str, parent_id: Optional[int] = None) -> Optional[Category]:
        # Check if category with the same name exists
        existing_category = self.category_repository.find_by_name(name)
        if existing_category:
            logger.error(f"Category name already exists: {name}")
            return None

        category = Category(name=name, parent_id=parent_id)
        self.category_repository.add_category(category)
        logger.info(f"Category added successfully: {name}")
        return category

    def list_all_categories(self) -> List[Dict[str, Any]]:
        categories = self.category_repository.list_all_categories()
        return [{'id': category.id, 'name': category.name, 'parent_id': category.parent_id} for category in categories]