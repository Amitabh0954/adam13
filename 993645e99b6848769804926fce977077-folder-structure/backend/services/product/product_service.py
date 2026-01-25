from backend.repositories.product.product_repository import ProductRepository
from backend.repositories.product.update_product_repository import UpdateProductRepository
from backend.models.product import Product

class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.update_product_repository = UpdateProductRepository()

    def update_product(self, product_id: int, name: str, price: float, description: str) -> None:
        product = self.update_product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        if name:
            if self.product_repository.get_product_by_name(name) and self.product_repository.get_product_by_name(name).id != product_id:
                raise ValueError("Product name already exists")
            product.name = name

        if price is not None:
            if price <= 0:
                raise ValueError("Product price must be a positive number")
            product.price = price

        if description:
            product.description = description
    
        self.update_product_repository.update_product(product)