# Epic Title: Product Catalog Management

from typing import Optional, List, Dict
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

    def update_product(self, product_id: int, name: str, price: float, description: str) -> bool:
        if price <= 0:
            logger.error(f"Invalid product price: {price}")
            return False

        product = self.product_repository.find_by_id(product_id)
        if not product:
            logger.error(f"Product not found: {product_id}")
            return False

        # Update only if new values are provided
        product.name = name if name else product.name
        product.price = price if price else product.price
        product.description = description if description else product.description

        self.product_repository.update_product(product)
        logger.info(f"Product updated successfully: {product_id}")
        return True

    def delete_product(self, product_id: int) -> bool:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            logger.error(f"Product not found: {product_id}")
            return False

        self.product_repository.delete_product(product)
        logger.info(f"Product deleted successfully: {product_id}")
        return True

    def search_products(self, query: str, page: int, per_page: int) -> List[Dict[str, Any]]:
        products = self.product_repository.search(query, page, per_page)
        logger.info(f"Search for query '{query}' returned {len(products)} products")
        return [self.format_product_result(product, query) for product in products]
    
    def format_product_result(self, product: Product, query: str) -> Dict[str, Any]:
        highlighted_name = product.name.replace(query, f"<b>{query}</b>")
        highlighted_description = product.description.replace(query, f"<b>{query}</b>")
        return {
            'id': product.id,
            'name': highlighted_name,
            'price': product.price,
            'description': highlighted_description
        }