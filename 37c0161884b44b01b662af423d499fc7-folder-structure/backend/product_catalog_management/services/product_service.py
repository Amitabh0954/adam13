# Epic Title: Add New Product

from typing import Optional
from product_catalog_management.repositories.product_repository import ProductRepository
from product_catalog_management.models.product import Product

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_new_product(self, name: str, price: float, description: str) -> Optional[Product]:
        if self.product_repository.get_product_by_name(name) or price <= 0 or not description:
            return None
        
        return self.product_repository.create_product(name, price, description)