# Epic Title: Search Products

from catalog.repositories.search_repository import SearchRepository
from catalog.models.product import Product
from django.core.paginator import Paginator
from typing import List, Tuple

class SearchService:
    def __init__(self):
        self.search_repository = SearchRepository()

    def search_products(self, query: str, page: int, page_size: int) -> Tuple[List[Product], int]:
        products = self.search_repository.search_products(query)
        paginator = Paginator(products, page_size)
        paginated_products = paginator.get_page(page)
        return list(paginated_products), paginator.count