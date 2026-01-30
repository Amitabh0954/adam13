# Epic Title: Delete Product

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

    def update_product(self, product: Product, **kwargs) -> Product:
        for attr, value in kwargs.items():
            setattr(product, attr, value)
        product.save()
        return product

    def delete_product(self, product: Product) -> None:
        product.delete()