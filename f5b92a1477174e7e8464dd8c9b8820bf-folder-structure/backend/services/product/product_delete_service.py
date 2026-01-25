from backend.repositories.product.product_repository import ProductRepository

class ProductDeleteService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> None:
        if not self.product_repository.get_product_by_id(product_id):
            raise ValueError("Product not found")

        self.product_repository.delete_product(product_id)