from backend.repositories.product.product_repository import ProductRepository

class ProductService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, price: float, description: str, category_id: int = None):
        return self.product_repository.add_product(name, price, description, category_id)

    def update_product(self, product_id: int, name: str = None, price: float = None, description: str = None):
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        
        if name:
            product.name = name
        if price is not None:
            if price <= 0:
                raise ValueError("Price must be a positive number")
            product.price = price
        if description is not None:
            if not description:
                raise ValueError("Description cannot be empty")
            product.description = description

        self.product_repository.save_product(product)

    def delete_product(self, product_id: int) -> None:
        self.product_repository.delete_product(product_id)