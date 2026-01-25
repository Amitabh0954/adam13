import logging
from backend.models.category import Category
from backend.database import db

logger = logging.getLogger(__name__)

class CategoryRepository:

    def create_category(self, name: str, parent_id: int = None) -> Category:
        if parent_id and not self.get_category_by_id(parent_id):
            raise ValueError("Parent category not found")
        
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        logger.info(f"Category created with name: {name}")
        return category

    def get_category_by_id(self, category_id: int) -> Category:
        return Category.query.get(category_id)

    def get_all_categories(self):
        return Category.query.all()