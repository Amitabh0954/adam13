from product_catalog_management.models import Product, Category
from product_catalog_management.extensions import db
from sqlalchemy import or_

class ProductRepository:
    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)

    def get_categories_by_ids(self, category_ids: list) -> list:
        return Category.query.filter(Category.id.in_(category_ids)).all()

    def delete_product(self, product: Product) -> None:
        product.is_active = False
        db.session.commit()

    def search_products(self, search_term: str, page: int, per_page: int):
        return Product.query.filter(
            Product.is_active,
            or_(
                Product.name.like(f'%{search_term}%'),
                Product.description.like(f'%{search_term}%'),
                Product.categories.any(Category.name.like(f'%{search_term}%'))
            )
        ).paginate(page, per_page, False)