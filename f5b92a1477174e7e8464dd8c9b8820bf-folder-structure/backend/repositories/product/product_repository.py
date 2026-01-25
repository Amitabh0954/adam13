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