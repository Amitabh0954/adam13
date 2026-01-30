# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository

class AddProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category: str) -> dict:
        if not name or not description or price <= 0:
            return {"error": "Invalid product data"}

        if self.product_repository.get_product_by_name(name):
            return {"error": "Product name already exists"}

        self.product_repository.create_product(name, description, price, category)
        return {"message": "Product added successfully"}