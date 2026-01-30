# Epic Title: Add New Product

from catalog.models.product import Product
from typing import Optional

class ProductRepository:

    def add_product(self, name: str, description: str, price: float, category_id: int) -> Product:
        product = Product(
            name=name,
            description=description,
            price=price,
            category_id=category_id
        )
        product.save()
        return product

    def get_product_by_name(self, name: str) -> Optional[Product]:
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            return None