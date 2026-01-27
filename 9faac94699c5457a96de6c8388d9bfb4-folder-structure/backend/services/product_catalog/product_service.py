# Epic Title: Product Catalog Management

from backend.repositories.product_catalog.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float) -> dict:
        if self.product_repository.get_product_by_name(name):
            return {'status': 'error', 'message': 'Product name already exists'}

        if price <= 0:
            return {'status': 'error', 'message': 'Price must be a positive number'}

        if not description:
            return {'status': 'error', 'message': 'Description cannot be empty'}

        self.product_repository.create_product(name, description, price)
        return {'status': 'success', 'message': 'Product added successfully'}