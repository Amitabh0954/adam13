# Epic Title: Product Catalog Management

from backend.product_catalog_management.repositories.product_repository import ProductRepository
from typing import Dict

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int) -> Dict[str, str]:
        if self.product_repository.get_product_by_name(name):
            return {'status': 'error', 'message': 'Product name already exists'}

        self.product_repository.add_product(name, description, price, category_id)
        return {'status': 'success', 'message': 'Product added successfully'}

    def update_product(self, product_id: int, name: str, description: str, price: float, category_id: int) -> Dict[str, str]:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {'status': 'error', 'message': 'Product not found'}

        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if category_id:
            product.category_id = category_id

        self.product_repository.update_product(product)
        return {'status': 'success', 'message': 'Product updated successfully'}