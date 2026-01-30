# Epic Title: Add New Product

from backend.models.product import Product
from typing import Optional, List

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