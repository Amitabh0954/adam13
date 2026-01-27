from product_catalog_management.models import Category
from product_catalog_management.extensions import db

class CategoryRepository:
    def get_category_by_id(self, category_id: int) -> Category:
        return Category.query.get(category_id)

    def get_category_by_name(self, name: str) -> Category:
        return Category.query.filter_by(name=name).first()

    def create_category(self, name: str, parent: Category) -> Category:
        new_category = Category(name=name, parent=parent)
        db.session.add(new_category)
        db.session.commit()
        return new_category

    def get_all_categories(self) -> list:
        return Category.query.all()

    def update_category(self, category: Category) -> None:
        db.session.commit()

    def delete_category(self, category: Category) -> None:
        db.session.delete(category)
        db.session.commit()