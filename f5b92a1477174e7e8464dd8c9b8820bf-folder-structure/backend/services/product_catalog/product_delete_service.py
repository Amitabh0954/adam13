from backend.repositories.product.product_delete_repository import ProductDeleteRepository

class ProductDeleteService:

    def __init__(self):
        self.product_delete_repository = ProductDeleteRepository()

    def delete_product(self, product_id: int):
        self.product_delete_repository.delete_product(product_id)