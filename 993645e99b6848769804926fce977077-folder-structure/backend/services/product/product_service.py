from backend.repositories.product.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str) -> None:
        if self.product_repository.get_product_by_name(name):
            raise ValueError("Product name already exists")

        if price <= 0:
            raise ValueError("Product price must be a positive number")

        new_product = Product(name=name, price=price, description=description)
        self.product_repository.save_product(new_product)