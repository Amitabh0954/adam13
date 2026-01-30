# Epic Title: Update Product Details

from products.models.product import Product
from typing import Optional, List

class ProductRepository:

    def add_product(self, name: str, description: str, price: float) -> Product:
        product = Product(name=name, description=description, price=price)
        product.save()
        return product

    def get_product_by_name(self, name: str) -> Optional[Product]:
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            return None

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get_all_products(self) -> List[Product]:
        return list(Product.objects.all())

# This file redefinition here allows safe addition of new methods without forward reference issues.