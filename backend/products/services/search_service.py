# Epic Title: Search Products

from backend.products.repositories.product_repository import ProductRepository
from backend.products.models.product import Product
from typing import List
import logging

logger = logging.getLogger(__name__)

class SearchService:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def search(self, query: str, page: int = 0, per_page: int = 10) -> List[Product]:
        products = self.product_repository.search_products(query, page, per_page)
        logger.info(f"Search completed with query: {query}")
        return products