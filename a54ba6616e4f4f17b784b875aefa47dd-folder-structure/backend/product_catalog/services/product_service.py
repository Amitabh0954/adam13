# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: str, price: float, description: str) -> dict:
        if product_id is None:
            return {"error": "Product ID is required"}

        if price is not None and (not isinstance(price, (int, float)) or price <= 0):
            return {"error": "Product price must be a positive number"}
        
        if description is not None and description.strip() == "":
            return {"error": "Product description cannot be empty"}

        if name and self.product_repository.product_name_exists_with_different_id(product_id, name):
            return {"error": "Product name already exists"}

        updated = self.product_repository.update_product(product_id, name, price, description)
        if updated:
            return {"message": "Product updated successfully"}
        return {"error": "Failed to update product"}