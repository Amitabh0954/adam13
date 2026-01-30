# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class UpdateProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, data: dict) -> dict:
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        if name is None or price is None or description is None:
            return {"error": "All fields are required"}

        if not isinstance(price, (int, float)) or price <= 0:
            return {"error": "Product price must be a positive number"}

        if not description.strip():
            return {"error": "Product description cannot be empty"}

        success = self.product_repository.update_product(product_id, name, price, description)
        if success:
            return {"message": "Product updated successfully"}
        return {"error": "Product update failed"}