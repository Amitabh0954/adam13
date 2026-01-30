# Epic Title: Add New Product

from backend.products.repositories.product_repository import ProductRepository
from backend.products.models.product import Product
import logging

logger = logging.getLogger(__name__)

class ProductService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def create_product(self, name: str, description: str, price: float) -> Product:
        existing_product = self.product_repository.get_product_by_name(name)
        if existing_product:
            raise ValueError("A product with this name already exists")
        
        product = self.product_repository.add_product(name, description, price)
        logger.info(f"Product {name} added to the inventory")
        return product

    def get_product(self, name: str) -> Product:
        product = self.product_repository.get_product_by_name(name)
        if not product:
            raise ValueError("Product not found")
        
        logger.info(f"Product retrieved: {product.name}")
        return product

    def list_products(self) -> list[Product]:
        products = self.product_repository.list_all_products()
        logger.info("Retrieved all products")
        return products