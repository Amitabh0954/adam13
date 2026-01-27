from backend.products.models.category import Category
from backend.auth.extensions import db

class CategoryRepository:
    def create_category(self, name: str, parent_id: int = None) -> Category:
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        return category

    def get_all_categories(self) -> list[Category]:
        return Category.query.all()

    def get_category_by_id(self, category_id: int) -> Category:
        return Category.query.filter_by(id=category_id).first()

    def update_category(self, category: Category) -> Category:
        db.session.commit()
        return category

    def delete_category(self, category_id: int):
        category = self.get_category_by_id(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()