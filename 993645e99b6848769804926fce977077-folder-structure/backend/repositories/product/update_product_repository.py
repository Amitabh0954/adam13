import logging
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class UpdateProductRepository:

    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.filter_by(id=product_id).first()
    
    def update_product(self, product: Product) -> None:
        db.session.commit()
        logger.info(f"Product updated: {product.id}")