# Epic Title: Search Products

from product_catalog_management.repositories.product_repository import ProductRepository
from product_catalog_management.models.product import Product
from typing import Optional, List

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

    def search_products(self, query: str, page: int = 1, items_per_page: int = 10) -> List[Product]:
        return self.product_repository.search_products(query, page, items_per_page)