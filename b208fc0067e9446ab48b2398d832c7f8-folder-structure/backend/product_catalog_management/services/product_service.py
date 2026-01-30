# Epic Title: Delete Product

from product_catalog_management.repositories.product_repository import ProductRepository
from product_catalog_management.models.product import Product
from typing import Optional

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_new_product(self, name: str, price: float, description: str) -> Optional[Product]:
        if price <= 0 or not description.strip():
            return None
        if self.product_repository.get_product_by_name(name):
            return None
        return self.product_repository.create_product(name, price, description)

    def update_product_details(self, name: str, **kwargs) -> Optional[Product]:
        product = self.product_repository.get_product_by_name(name)
        if product:
            return self.product_repository.update_product(product, **kwargs)
        return None

    def delete_product(self, name: str) -> bool:
        product = self.product_repository.get_product_by_name(name)
        if product:
            self.product_repository.delete_product(product)
            return True
        return False