# Epic Title: Add New Product

from catalog.repositories.product_repository import ProductRepository
from typing import Tuple

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int) -> Tuple[bool, str]:
        if self.product_repository.get_product_by_name(name):
            return False, 'Product name must be unique'
        
        product = self.product_repository.add_product(name, description, price, category_id)
        return True, 'Product added successfully'