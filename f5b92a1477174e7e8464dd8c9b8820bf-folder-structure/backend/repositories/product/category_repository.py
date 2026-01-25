import logging
from backend.models.product import Category
from backend.database import db

logger = logging.getLogger(__name__)

class CategoryRepository:

    def add_category(self, name: str, parent_id: int = None) -> Category:
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        logger.info(f"Category '{name}' added to the database")
        return category

    def update_category(self, category_id: int, name: str = None, parent_id: int = None) -> Category:
        category = Category.query.get(category_id)
        if not category:
            raise ValueError("Category not found")
        
        if name:
            category.name = name

        category.parent_id = parent_id
        db.session.commit()
        logger.info(f"Category '{name}' updated in the database")
        return category