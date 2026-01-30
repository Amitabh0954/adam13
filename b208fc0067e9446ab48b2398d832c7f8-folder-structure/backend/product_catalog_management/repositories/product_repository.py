# Epic Title: Add New Product

from product_catalog_management.models.product import Product
from typing import Optional

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