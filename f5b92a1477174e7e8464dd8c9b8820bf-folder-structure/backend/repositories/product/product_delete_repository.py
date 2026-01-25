import logging
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class ProductDeleteRepository:

    def delete_product(self, product_id: int):
        product = Product.query.get(product_id)
        if not product:
            raise ValueError("Product not found")
        
        db.session.delete(product)
        db.session.commit()
        logger.info(f"Product with ID '{product_id}' deleted from the database")