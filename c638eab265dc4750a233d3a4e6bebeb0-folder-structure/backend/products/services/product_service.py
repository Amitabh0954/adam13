# Epic Title: Add New Product

from products.repositories.product_repository import ProductRepository
from products.models.product import Product
from typing import Optional, List

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float) -> Optional[Product]:
        if self.product_repository.get_product_by_name(name):
            return None
        return self.product_repository.add_product(name, description, price)

    def get_all_products(self) -> List[Product]:
        return self.product_repository.get_all_products()