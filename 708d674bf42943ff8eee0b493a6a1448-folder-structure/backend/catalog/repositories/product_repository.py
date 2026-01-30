# Epic Title: Add New Product

from catalog.models.product import Product
from typing import Optional, List

class ProductRepository:

    def create_product(self, name: str, description: str, price: float) -> Product:
        product = Product(name=name, description=description, price=price)
        product.save()
        return product

    def get_product_by_name(self, name: str) -> Optional[Product]:
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            return None

    def get_all_products(self) -> List[Product]:
        return list(Product.objects.all())