# Epic Title: Product Catalog Management

from backend.repositories.product_repository import ProductRepository
from typing import Dict

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int) -> Dict[str, str]:
        if self.product_repository.get_product_by_name(name):
            return {'status': 'error', 'message': 'Product name must be unique'}

        if price <= 0:
            return {'status': 'error', 'message': 'Product price must be a positive number'}

        if not description:
            return {'status': 'error', 'message': 'Product description cannot be empty'}

        self.product_repository.create_product(name, description, price, category_id)
        return {'status': 'success', 'message': 'Product added successfully'}

    def update_product(self, product_id: int, name: str, description: str, price: float, category_id: int) -> Dict[str, str]:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {'status': 'error', 'message': 'Product not found'}
        
        if name and product.name != name:
            if self.product_repository.get_product_by_name(name):
                return {'status': 'error', 'message': 'Product name must be unique'}
            product.name = name

        if price is not None:
            if price <= 0:
                return {'status': 'error', 'message': 'Product price must be a positive number'}
            product.price = price

        if description:
            product.description = description
        elif description == "":
            return {'status': 'error', 'message': 'Product description cannot be empty'}

        if category_id:
            product.category_id = category_id

        self.product_repository.update_product(product)
        return {'status': 'success', 'message': 'Product updated successfully'}

    def delete_product(self, product_id: int) -> Dict[str, str]:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {'status': 'error', 'message': 'Product not found'}

        self.product_repository.delete_product(product)
        return {'status': 'success', 'message': 'Product deleted successfully'}