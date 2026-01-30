# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: str | None, price: float | None, description: str | None) -> dict:
        if name is not None and self.product_repository.is_name_taken(name, product_id):
            return {"error": "Product name already exists"}
        
        success = self.product_repository.update_product(product_id, name, price, description)
        if success:
            return {"message": "Product updated successfully"}
        return {"error": "Failed to update product"}