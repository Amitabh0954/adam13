# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        success = self.product_repository.delete_product(product_id)
        if success:
            return {"message": "Product deleted successfully"}
        return {"error": "Failed to delete product"}