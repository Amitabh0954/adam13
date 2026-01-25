import logging
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class ProductRepository:
    
    def add_product(self, name: str, price: float, description: str, category_id: int) -> Product:
        if self.get_product_by_name(name):
            raise ValueError("Product name must be unique")

        product = Product(name=name, price=price, description=description, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        logger.info(f"Product added with name: {name}")
        return product

    def get_product_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)

    def save_product(self, product: Product) -> None:
        db.session.commit()
        logger.info(f"Product updated with ID: {product.id}")

    def delete_product(self, product_id: int) -> None:
        product = self.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        
        db.session.delete(product)
        db.session.commit()
        logger.info(f"Product deleted with ID: {product_id}")

    def search_products(self, query: str, page: int, per_page: int):
        search_query = f"%{query}%"
        products = Product.query.filter(
            db.or_(
                Product.name.ilike(search_query),
                Product.description.ilike(search_query),
                Product.category.has(name.ilike(search_query))
            )
        ).paginate(page, per_page, False)
        return products.items, products.total