# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository

class DeleteProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {"error": "Product not found"}

        deleted = self.product_repository.delete_product(product_id)
        if deleted:
            return {"message": "Product deleted successfully"}
        return {"error": "Failed to delete product"}