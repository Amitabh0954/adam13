from backend.repositories.catalog_management.product_repository import ProductRepository
from backend.repositories.catalog_management.category_repository import CategoryRepository
from backend.models.product import Product

class ProductService:
    # Inline comment referencing the Epic Title
    # Epic Title: Shopping Cart Functionality

    def __init__(self):
        self.product_repository = ProductRepository()
        self.category_repository = CategoryRepository()

    def add_product(self, data: dict) -> dict:
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        category_ids = data.get("category_ids", [])

        if not name or self.product_repository.find_by_name(name):
            raise ValueError("Product name must be unique.")
        
        if not price or price <= 0:
            raise ValueError("Product price must be a positive number.")
        
        if not description:
            raise ValueError("