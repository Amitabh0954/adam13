# Epic Title: Product Catalog Management
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, search_term: str, page: int, page_size: int) -> dict:
        if not search_term:
            return {"error": "Search term cannot be empty"}

        results, total = self.product_repository.search_products(search_term, page, page_size)
        total_pages = (total // page_size) + (1 if total % page_size > 0 else 0)

        return {
            "results": results,
            "total": total,
            "page": page,
            "total_pages": total_pages
        }