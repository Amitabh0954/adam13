# Epic Title: Delete Product

from backend.repositories.product_repository import ProductRepository
from typing import Tuple

class ProductDeleteService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> Tuple[bool, str]:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return False, 'Product not found'
        
        product.delete()
        return True, 'Product deleted successfully'