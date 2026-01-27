# Epic Title: Product Catalog Management

from backend.repositories.product_catalog.product_repository import ProductRepository

class ProductDeleteService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {'status': 'error', 'message': 'Product not found'}

        self.product_repository.delete_product(product)
        return {'status': 'success', 'message': 'Product deleted successfully'}