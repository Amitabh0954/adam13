# Epic Title: Search Products

from catalog.repositories.search_product_repository import SearchProductRepository
from catalog.models.product import Product
from typing import List

class SearchService:
    def __init__(self):
        self.search_product_repository = SearchProductRepository()

    def search_products(self, query: str) -> List[Product]:
        return self.search_product_repository.search_products(query)

    def highlight_search_terms(self, product: Product, query: str) -> str:
        highlighted_description = product.description.replace(query, f"<strong>{query}</strong>")
        return highlighted_description