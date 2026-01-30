# Epic Title: Add New Product

from backend.repositories.product_repository import ProductRepository
from typing import Tuple, Optional

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str) -> Tuple[bool, str]:
        if self.product_repository.get_product_by_name(name):
            return False, 'Product name must be unique'

        if price <= 0:
            return False, 'Product price must be a positive number'

        if not description:
            return False, 'Product description cannot be empty'

        self.product_repository.add_product(name, price, description)
        return True, 'Product added successfully'

    def get_all_products(self) -> Optional[List[dict]]:
        products = self.product_repository.get_all_products()
        if not products:
            return None
        
        products_data = [
            {
                'name': product.name,
                'price': product.price,
                'description': product.description,
            }
            for product in products
        ]
        return products_data