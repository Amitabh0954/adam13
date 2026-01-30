# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class AddProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, data: dict) -> dict:
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        if not name or not price or not description:
            return {"error": "All fields are required"}

        if price <= 0:
            return {"error": "Product price must be a positive number"}

        if self.product_repository.is_name_taken(name):
            return {"error": "Product name must be unique"}

        product_id = self.product_repository.create_product(name, price, description)
        return {"product_id": product_id, "message": "Product added successfully"}