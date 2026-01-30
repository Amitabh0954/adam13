# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        if product_id is None:
            return {"error": "Product ID is required"}

        deleted = self.product_repository.delete_product(product_id)
        if deleted:
            return {"message": "Product deleted successfully"}
        return {"error": "Failed to delete product"}