from backend.models.category import Category
from backend.extensions import db

class CategoryRepository:
    def find_by_id(self, category_id: int) -> Category:
        return Category.query.get(category_id)
    
    def find_by_name(self, name: str) -> Category:
        return Category.query.filter_by(name=name).first()

    def save_category(self, category: Category):
        db.session.add(category)
        db.session.commit()

    def delete_category(self, category: Category):
        db.session.delete(category)
        db.session.commit()

    def update_category(self, category: Category):
        db.session.commit()