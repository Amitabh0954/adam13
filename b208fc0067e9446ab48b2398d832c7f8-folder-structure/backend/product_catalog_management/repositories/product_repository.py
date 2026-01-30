# Epic Title: Search Products

from product_catalog_management.models.product import Product
from typing import Optional, List
from django.db.models import Q

class ProductRepository:

    def create_product(self, name: str, price: float, description: str) -> Product:
        product = Product(name=name, price=price, description=description)
        product.save()
        return product

    def get_product_by_name(self, name: str) -> Optional[Product]:
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            return None

    def update_product(self, product: Product, **kwargs) -> Product:
        for attr, value in kwargs.items():
            setattr(product, attr, value)
        product.save()
        return product

    def delete_product(self, product: Product) -> None:
        product.delete()

    def search_products(self, query: str, page: int = 1, items_per_page: int = 10) -> List[Product]:
        offset = (page - 1) * items_per_page
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )[offset: offset + items_per_page]
        return list(products)