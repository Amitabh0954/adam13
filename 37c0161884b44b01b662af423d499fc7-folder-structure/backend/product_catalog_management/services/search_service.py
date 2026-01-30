# Epic Title: Search Products

from typing import List, Optional
from product_catalog_management.repositories.product_repository import ProductRepository
from product_catalog_management.models.product import Product

class SearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, search_term: str, page: int, page_size: int) -> List[Product]:
        start = (page - 1) * page_size
        end = start + page_size
        return self.product_repository.search_products(search_term)[start:end]