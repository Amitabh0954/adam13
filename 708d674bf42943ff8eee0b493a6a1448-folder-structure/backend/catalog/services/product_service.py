# Epic Title: Update Product Details

from catalog.repositories.product_repository import ProductRepository
from catalog.models.product import Product
from typing import Optional, List

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float) -> Optional[Product]:
        if self.product_repository.get_product_by_name(name):
            return None
        return self.product_repository.create_product(name, description, price)

    def update_product(self, product_id: int, name: Optional[str], description: Optional[str], price: Optional[float]) -> Optional[Product]:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return None
        return self.product_repository.update_product(product, name, description, price)

    def get_all_products(self) -> List[Product]:
        return self.product_repository.get_all_products()