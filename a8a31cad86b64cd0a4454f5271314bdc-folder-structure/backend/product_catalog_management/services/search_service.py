# Epic Title: Product Catalog Management

from backend.product_catalog_management.repositories.product_repository import ProductRepository
from typing import Dict

class SearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int) -> Dict:
        results = self.product_repository.search_products(query, page, per_page)
        return {
            'total': results.total,
            'page': page,
            'per_page': per_page,
            'products': [{
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'category_id': product.category_id
            } for product in results.items]
        }