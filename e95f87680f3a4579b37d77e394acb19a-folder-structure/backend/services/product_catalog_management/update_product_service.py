# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository

class UpdateProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, data: dict) -> dict:
        if not data.get("price") or data["price"] <= 0:
            return {"error": "Invalid product price"}

        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {"error": "Product not found"}

        if data.get("description") is None:
            return {"error": "Product description cannot be removed"}

        updated = self.product_repository.update_product(product_id, data)
        if updated:
            return {"message": "Product updated successfully"}
        return {"error": "Failed to update product"}