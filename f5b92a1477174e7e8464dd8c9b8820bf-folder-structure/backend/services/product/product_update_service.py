from backend.repositories.product.product_repository import ProductRepository

class ProductUpdateService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: str, price: float, description: str) -> None:
        self.product_repository.update_product(product_id, name, price, description)