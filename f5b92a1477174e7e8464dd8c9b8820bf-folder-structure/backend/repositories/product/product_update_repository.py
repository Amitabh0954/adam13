import logging
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class ProductUpdateRepository:

    def update_product(self, product_id: int, name: str, price: float, description: str) -> Product:
        product = Product.query.get(product_id)
        if not product:
            raise ValueError("Product not found")

        if name:
            existing_product = Product.query.filter_by(name=name).first()
            if existing_product and existing_product.id != product_id:
                raise ValueError("Product name must be unique")
            product.name = name

        if price is not None:
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Product price must be a numeric value greater than zero")
            product.price = price

        if description:
            product.description = description

        db.session.commit()
        logger.info(f"Product '{product.name}' updated in the database")
        return product