# Epic Title: Search Products

from catalog.models.product import Product
from django.db.models import Q
from typing import List

class SearchProductRepository:

    def search_products(self, query: str) -> List[Product]:
        search_criteria = Q(name__icontains=query) | Q(description__icontains=query)
        return list(Product.objects.filter(search_criteria))