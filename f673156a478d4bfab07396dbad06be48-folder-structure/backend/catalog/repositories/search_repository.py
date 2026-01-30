# Epic Title: Search Products

from catalog.models.product import Product
from catalog.models.category import Category
from django.db.models import Q
from typing import List

class SearchRepository:

    def search_products(self, query: str) -> List[Product]:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(attributes__name__icontains=query)
        ).distinct()
        return products