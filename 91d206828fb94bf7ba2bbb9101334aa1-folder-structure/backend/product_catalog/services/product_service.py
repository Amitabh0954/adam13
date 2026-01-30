# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str) -> dict:
        if self.product_repository.exists_by_name(name):
            return {"error": "Product with this name already exists"}

        product_id = self.product_repository.create_product(name, price, description)
        
        if product_id:
            return {"product_id": product_id, "message": "Product added successfully"}
        return {"error": "Failed to add product"}