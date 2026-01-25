import logging
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class ProductRepository:

    def add_product(self, name: str, price: float, description: str, category_id: int) -> Product:
        existing_product = Product.query.filter_by(name=name).first()
        if existing_product:
            raise ValueError("Product name must be unique")

        if price <= 0:
            raise ValueError("Product price must be a positive number")

        if not description:
            raise ValueError("Product description cannot be empty")

        product = Product(name=name, price=price, description=description, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        logger.info(f"Product '{name}' added to the database")
        return product