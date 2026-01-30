# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str) -> dict:
        if self.product_repository.is_name_taken(name):
            return {"error": "Product name already exists"}
        
        if price <= 0:
            return {"error": "Product price must be a positive number"}
        
        if not description.strip():
            return {"error": "Product description cannot be empty"}

        product_id = self.product_repository.create_product(name, price, description)
        return {"product_id": product_id, "message": "Product added successfully"}