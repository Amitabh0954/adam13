from backend.repositories.product.product_repository import ProductRepository
from backend.repositories.product.delete_product_repository import DeleteProductRepository
from backend.models.product import Product

class ProductService:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.delete_product_repository = DeleteProductRepository()

    def delete_product(self, product_id: int) -> None:
        product = self.delete_product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        self.delete_product_repository.delete_product(product)