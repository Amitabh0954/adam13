# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository

class ProductSearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int = 1, page_size: int = 10) -> dict:
        offset = (page - 1) * page_size
        products = self.product_repository.search_products(query, offset, page_size)
        total_count = self.product_repository.count_search_results(query)
        
        for product in products:
            product['name'] = self.highlight_terms(product['name'], query)
            product['description'] = self.highlight_terms(product['description'], query)
        
        return {
            "results": products,
            "page": page,
            "total_pages": (total_count + page_size - 1) // page_size,
            "total_results": total_count
        }

    def highlight_terms(self, text: str, term: str) -> str:
        import re
        highlighted = re.sub(f"({re.escape(term)})", r"<em>\1</em>", text, flags=re.IGNORECASE)
        return highlighted