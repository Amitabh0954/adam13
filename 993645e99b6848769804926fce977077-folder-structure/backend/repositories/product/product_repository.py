import logging
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class ProductRepository:
    
    def get_product_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()
    
    def save_product(self, product: Product) -> None:
        db.session.add(product)
        db.session.commit()
        logger.info(f"Product saved with name: {product.name}")