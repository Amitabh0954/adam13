# Epic Title: Product Catalog Management

from typing import Optional, List, Dict
from backend.repositories.product_catalog.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_product(self, name: str, price: float, description: str, category: str) -> Optional[str]:
        if not name:
            return "Product name cannot be empty"
        if self.product_repository.find_product_by_name(name):
            return "Product name must be unique"
        if price <= 0:
            return "Product price must be a positive number"
        if not description:
            return "Product description cannot be empty"

        self.product_repository.add_product(name, price, description, category)
        return None

    def update_product(self, product_id: int, price: Optional[float] = None, description: Optional[str] = None, category: Optional[str] = None) -> Optional[str]:
        if price is not None and price <= 0:
            return "Product price must be a positive number"
        if description is not None and not description:
            return "Product description cannot be empty"

        self.product_repository.update_product(product_id, price, description, category)
        return None

    def delete_product(self, product_id: int) -> None:
        self.product_repository.delete_product(product_id)

    def search_products(self, term: str, page: int, per_page: int) -> List[Dict[str, str]]:
        return self.product_repository.search_products(term, page, per_page)