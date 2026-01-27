from product_catalog_management.models import Product, Category
from product_catalog_management.extensions import db

class ProductRepository:
    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)

    def get_categories_by_ids(self, category_ids: list) -> list:
        return Category.query.filter(Category.id.in_(category_ids)).all()

    def update_product(self, product: Product) -> None:
        db.session.commit()