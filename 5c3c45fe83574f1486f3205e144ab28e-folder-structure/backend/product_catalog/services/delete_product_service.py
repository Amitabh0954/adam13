# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class DeleteProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        if not self.product_repository.product_exists(product_id):
            return {"error": "Product not found"}

        success = self.product_repository.delete_product_by_id(product_id)
        if success:
            return {"message": "Product deleted successfully"}
        
        return {"error": "Failed to delete product"}