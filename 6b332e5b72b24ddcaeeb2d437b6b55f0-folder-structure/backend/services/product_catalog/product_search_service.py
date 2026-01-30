# Epic Title: Search Products

from backend.repositories.product_repository import ProductRepository
from typing import List, Optional

class ProductSearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int = 1, page_size: int = 10) -> Optional[List[dict]]:
        products = self.product_repository.search_products(query, page, page_size)
        if not products:
            return None
        
        products_data = [
            {
                'name': product.name,
                'price': product.price,
                'description': product.description,
            }
            for product in products
        ]
        return products_data