# Epic Title: Product Categorization

from products.repositories.product_repository import ProductRepository
from products.models.product import Product
from categories.models.category import Category
from typing import Optional, List

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int) -> Optional[Product]:
        if self.product_repository.get_product_by_name(name):
            return None
        category = Category.objects.get(id=category_id)
        return self.product_repository.add_product(name, description, price, category)

    def get_all_products(self) -> List[Product]:
        return self.product_repository.get_all_products()

    def update_product(self, product_id: int, name: str, description: str, price: float) -> Optional[Product]:
        product = self.product_repository.get_product_by_id(product_id)
        if product:
            product.name = name
            product.description = description
            product.price = price
            product.save()
            return product
        return None

    def delete_product(self, product_id: int) -> bool:
        return self.product_repository.delete_product_by_id(product_id)