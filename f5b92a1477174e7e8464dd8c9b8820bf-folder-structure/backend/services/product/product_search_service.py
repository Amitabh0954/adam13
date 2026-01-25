from backend.repositories.product.product_repository import ProductRepository

class ProductSearchService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int):
        return self.product_repository.search_products(query, page, per_page)