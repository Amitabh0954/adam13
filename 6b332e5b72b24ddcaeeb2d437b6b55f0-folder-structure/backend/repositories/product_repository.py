# Epic Title: Search Products

from backend.models.product import Product
from typing import List, Optional

class ProductRepository:

    def add_product(self, name: str, price: float, description: str) -> Product:
        product = Product(
            name=name,
            price=price,
            description=description,
        )
        product.save()
        return product

    def get_product_by_name(self, name: str) -> Optional[Product]:
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            return None

    def get_all_products(self) -> List[Product]:
        return Product.objects.all()

    def search_products(self, query: str, page: int, page_size: int) -> List[Product]:
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
        return products[(page - 1) * page_size: page * page_size]