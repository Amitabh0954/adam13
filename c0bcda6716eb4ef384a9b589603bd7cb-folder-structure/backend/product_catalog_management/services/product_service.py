# Epic Title: Product Catalog Management

from typing import Optional
from structured_logging import get_logger
from backend.product_catalog_management.repositories.product_repository import ProductRepository
from backend.product_catalog_management.models.product import Product

logger = get_logger(__name__)

class ProductService:
    
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
    
    def add_product(self, name: str, price: float, description: str) -> Optional[Product]:
        if not name or not description:
            logger.error(f"Invalid product details: {name}, {description}")
            return None

        if price <= 0:
            logger.error(f"Invalid product price: {price}")
            return None

        existing_product = self.product_repository.find_by_name(name)
        if existing_product:
            logger.error(f"Product name already exists: {name}")
            return None
        
        product = Product(name, price, description)
        self.product_repository.add_product(product)
        logger.info(f"Product added successfully: {name}")
        return product