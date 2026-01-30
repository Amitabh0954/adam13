# Epic Title: Product Catalog Management
from typing import List, Dict
from repositories.product_repository import ProductRepository

class SearchProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, page_size: int) -> Dict[str, any]:
        results = self.product_repository.search_products(query, page, page_size)
        total_results = self.product_repository.count_search_results(query)
        
        return {
            "total_results": total_results,
            "page": page,
            "page_size": page_size,
            "results": results
        }