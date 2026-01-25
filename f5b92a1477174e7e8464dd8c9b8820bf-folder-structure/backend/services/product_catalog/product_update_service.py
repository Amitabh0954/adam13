from backend.repositories.product.product_update_repository import ProductUpdateRepository

class ProductUpdateService:

    def __init__(self):
        self.product_update_repository = ProductUpdateRepository()

    def update_product(self, product_id: int, name: str, price: float, description: str):
        return self.product_update_repository.update_product(product_id, name, price, description)