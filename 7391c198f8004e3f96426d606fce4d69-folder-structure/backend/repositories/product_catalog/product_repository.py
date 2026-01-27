from product_catalog_management.models import Product, Category
from product_catalog_management.extensions import db

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    def get_categories_by_ids(self, category_ids: list) -> list:
        return Category.query.filter(Category.id.in_(category_ids)).all()

    def create_product(self, name: str, price: float, description: str, categories: list) -> Product:
        new_product = Product(name=name, price=price, description=description, categories=categories)
        db.session.add(new_product)
        db.session.commit()
        return new_product