# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository

class ProductDeletionService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        existing_product = self.product_repository.get_product_by_id(product_id)
        if not existing_product:
            return {"error": "Product not found"}

        # Ensure only admin can delete products; placeholder check
        if not self._is_admin():
            return {"error": "Only admin can delete product details"}

        success = self.product_repository.delete_product(product_id)
        if not success:
            return {"error": "Failed to delete product"}

        return {"message": "Product deleted successfully"}

    def _is_admin(self) -> bool:
        # Placeholder for actual admin check; can be replaced with real authentication logic
        return True