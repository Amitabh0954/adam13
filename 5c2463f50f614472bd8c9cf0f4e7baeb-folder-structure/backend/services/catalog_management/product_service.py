from backend.repositories.catalog_management.product_repository import ProductRepository
from backend.models.product import Product
from backend.models.user import User

class ProductService:
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

    def update_product(self, user: User, product_id: int, data: dict) -> dict:
        if not user.is_admin:
            raise ValueError("Only admins can update the product details.")
        
        product = self.product_repository.find_by_id(product_id)
        
        if not product:
            raise ValueError("Product not found.")
        
        if 'price' in data:
            price = data['price']
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Product price must be a positive number.")
            product.price = price
        
        if 'description' in data:
            description = data['description']
            if description:
                product.description = description
            else:
                raise ValueError("Product description cannot be empty.")
        
        self.product_repository.update_product(product)
        return product.to_dict()

    def delete_product(self, user: User, product_id: int):
        if not user.is_admin:
            raise ValueError("Only admins can delete products.")
        
        product = self.product_repository.find_by_id(product_id)
        
        if not product:
            raise ValueError("Product not found.")
        
        self.product_repository.delete_product(product)