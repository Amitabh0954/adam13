from backend.repositories.catalog_management.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    # Inline comment referencing the Epic Title
    # Epic Title: Product Catalog Management

    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, data: dict) -> dict:
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")

        if not name or self.product_repository.find_by_name(name):
            raise ValueError("Product name must be unique.")
        
        if not price or price <= 0:
            raise ValueError("Product price must be a positive number.")
        
        if not description:
            raise ValueError("Product description cannot be empty.")

        new_product = Product(name=name, price=price, description=description)
        self.product_repository.save_product(new_product)
        return new_product.to_dict()

    def update_product(self, product_id: int, data: dict) -> dict:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        name = data.get("name")
        price = data.get("price")
        description = data.get("description")

        if name and name != product.name:
            if self.product_repository.find_by_name(name):
                raise ValueError("Product name must be unique.")
            product.name = name
        
        if price is not None:
            if price <= 0:
                raise ValueError("Product price must be a positive number.")
            product.price = price
        
        if description:
            product.description = description

        self.product_repository.update_product(product)
        return product.to_dict()