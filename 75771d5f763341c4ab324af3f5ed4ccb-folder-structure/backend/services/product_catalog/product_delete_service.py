# Epic Title: Delete Product

from repositories.product_catalog.product_repository import ProductRepository

class ProductDeleteService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def delete_product(self, product_id: int) -> dict:
        self.product_repository.delete_product(product_id)
        return {"msg": "Product deleted successfully"}