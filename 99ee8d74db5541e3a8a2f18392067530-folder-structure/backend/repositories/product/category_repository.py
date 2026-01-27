# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.models.product import Category

class CategoryRepository:
    def get_category_by_name(self, name: str) -> Category:
        return db_session.query(Category).filter_by(name=name).first()

    def add_category(self, name: str, parent_id: int) -> Category:
        new_category = Category(name=name, parent_id=parent_id)
        db_session.add(new_category)
        db_session.commit()
        return new_category

    def get_category_by_id(self, category_id: int) -> Category:
        return db_session.query(Category).filter_by(id=category_id).first()

    def update_category(self, category: Category):
        db_session.add(category)
        db_session.commit()

    def delete_category(self, category: Category):
        db_session.delete(category)
        db_session.commit()