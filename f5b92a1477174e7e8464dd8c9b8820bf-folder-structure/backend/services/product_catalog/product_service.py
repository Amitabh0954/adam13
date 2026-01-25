from backend.repositories.product.product_repository import ProductRepository

class ProductService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str, category_id: int = None):
        return self.product_repository.add_product(name, price, description, category_id)