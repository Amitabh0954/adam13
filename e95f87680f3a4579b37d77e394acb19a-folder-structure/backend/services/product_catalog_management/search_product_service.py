# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository

class SearchProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int) -> dict:
        offset = (page - 1) * per_page
        products = self.product_repository.search_products(query, offset, per_page)
        return {"products": products, "page": page, "per_page": per_page, "total": len(products)}