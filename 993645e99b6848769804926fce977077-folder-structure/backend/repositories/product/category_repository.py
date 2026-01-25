import logging
from backend.models.category import Category
from backend.database import db

logger = logging.getLogger(__name__)

class CategoryRepository:
    
    def get_category_by_id(self, category_id: int) -> Category:
        return Category.query.filter_by(id=category_id).first()

    def get_category_by_name(self, name: str) -> Category:
        return Category.query.filter_by(name=name).first()
    
    def save_category(self, category: Category) -> None:
        db.session.add(category)
        db.session.commit()
        logger.info(f"Category saved with name: {category.name}")
    
    def delete_category(self, category: Category) -> None:
        db.session.delete(category)
        db.session.commit()
        logger.info(f"Category deleted: {category.id}")