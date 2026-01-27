# Epic Title: Product Catalog Management

from backend.repositories.product_catalog.product_repository import ProductRepository
from typing import List, Dict

class ProductSearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int) -> Dict:
        products = self.product_repository.search_products(query, page, per_page)
        total = self.product_repository.count_search_results(query)
        return {
            'products': products,
            'page': page,
            'per_page': per_page,
            'total': total
        }