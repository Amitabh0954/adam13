# Epic Title: Search Products

from products.models.product import Product
from typing import List, Dict
from django.db.models import Q

class SearchService:
    
    def search_products(self, query: str, page: int, page_size: int) -> List[Dict[str, str]]:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query)
        )[(page-1)*page_size: page*page_size]

        return [{'name': product.name, 'description': product.description, 'price': str(product.price), 'category': product.category} for product in products]