# Epic Title: Update Product Details

from backend.repositories.product_repository import ProductRepository
from typing import Tuple, Optional

class ProductUpdateService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: Optional[str], price: Optional[float], description: Optional[str]) -> Tuple[bool, str]:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return False, 'Product not found'
        
        if name:
            product.name = name
        
        if price is not None:
            if price <= 0:
                return False, 'Product price must be a positive number'
            product.price = price
        
        if description and description.strip():
            product.description = description
        
        product.save()
        return True, 'Product updated successfully'