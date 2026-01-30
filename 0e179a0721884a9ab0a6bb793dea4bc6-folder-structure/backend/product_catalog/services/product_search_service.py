# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository
import re

class ProductSearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int) -> dict:
        products = self.product_repository.search_products(query, page, per_page)
        highlighted_products = self.highlight_search_terms(products, query)
        total_results = self.product_repository.count_search_results(query)
        return {
            "results": highlighted_products,
            "total_results": total_results,
            "current_page": page,
            "per_page": per_page
        }

    def highlight_search_terms(self, products: list, query: str) -> list:
        query_terms = query.split()
        for product in products:
            for term in query_terms:
                regex = re.compile(re.escape(term), re.IGNORECASE)
                product['name'] = regex.sub(f'<strong>{term}</strong>', product['name'])
                product['description'] = regex.sub(f'<strong>{term}</strong>', product['description'])
        return products