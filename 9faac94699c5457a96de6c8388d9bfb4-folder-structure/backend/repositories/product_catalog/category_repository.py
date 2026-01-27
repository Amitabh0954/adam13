# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.models.category import Category
from typing import List

class CategoryRepository:
    def get_category_by_id(self, category_id: int) -> Category:
        return db_session.query(Category).filter_by(id=category_id).first()

    def create_category(self, name: str, parent_id: int = None) -> Category:
        new_category = Category(name=name, parent_id=parent_id)
        db_session.add(new_category)
        db_session.commit()
        return new_category

    def get_all_categories(self) -> List[Category]:
        return db_session.query(Category).all()