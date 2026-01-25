import logging
from backend.models.product import Category
from backend.database import db

logger = logging.getLogger(__name__)

class CategoryRepository:
    
    def add_category(self, name: str, parent_id: int = None) -> Category:
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        logger.info(f"Category added with name: {name}")
        return category

    def get_all_categories(self) -> list:
        categories = Category.query.all()
        return [category.to_dict() for category in categories]

    def get_category_by_id(self, category_id: int) -> Category:
        return Category.query.get(category_id)