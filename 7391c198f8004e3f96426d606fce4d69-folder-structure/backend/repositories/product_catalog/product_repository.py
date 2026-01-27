from product_catalog_management.models import Product, Category
from product_catalog_management.extensions import db

class ProductRepository:
    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)

    def delete_product(self, product: Product) -> None:
        product.is_active = False
        db.session.commit()