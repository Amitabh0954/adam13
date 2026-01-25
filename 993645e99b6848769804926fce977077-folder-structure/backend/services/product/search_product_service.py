from backend.repositories.product.search_product_repository import SearchProductRepository

class SearchProductService:
    
    def __init__(self):
        self.search_product_repository = SearchProductRepository()

    def search_products(self, query: str, page: int, per_page: int) -> dict:
        products_paginated = self.search_product_repository.search_products(query, page, per_page)

        products = [{
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "category": product.category
        } for product in products_paginated.items]

        return {
            "total": products_paginated.total,
            "page": page,
            "per_page": per_page,
            "products": products
        }