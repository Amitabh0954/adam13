from backend.repositories.product.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str) -> None:
        if self.product_repository.get_product_by_name(name):
            raise ValueError("Product with this name already exists")

        new_product = Product(name=name, price=price, description=description)
        self.product_repository.save_product(new_product)