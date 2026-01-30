# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository
from backend.models.product_catalog.product import Product

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, name: str, description: str, price: float, category_id: int) -> dict:
        if not Product.validate_name(name):
            return {"error": "Product name cannot be empty"}
        if not Product.validate_description(description):
            return {"error": "Product description cannot be empty"}
        if not Product.validate_price(price):
            return {"error": "Product price must be a positive number"}

        existing_product = self.product_repository.get_product_by_name(name)
        if existing_product:
            return {"error": "Product with the same name already exists"}

        product = Product(id=None, name=name, description=description, price=price, category_id=category_id)
        success = self.product_repository.add_product(product)
        if not success:
            return {"error": "Failed to add product"}

        return {"message": "Product added successfully"}