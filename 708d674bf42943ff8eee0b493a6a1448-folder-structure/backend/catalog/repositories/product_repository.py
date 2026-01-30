# Epic Title: Delete Product

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

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None
    
    def delete_product(self, product: Product) -> None:
        product.delete()

    def update_product(self, product: Product, name: Optional[str], description: Optional[str], price: Optional[float]) -> Product:
        if name is not None:
            product.name = name
        if description is not None:
            product.description = description
        if price is not None:
            product.price = price
        product.save()
        return product

    def get_all_products(self) -> List[Product]:
        return list(Product.objects.all())