# Epic Title: Product Catalog Management
from backend.repositories.product_repository import ProductRepository
from backend.models.product_catalog.product import Product

class ProductUpdateService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: str, description: str, price: float, category_id: int) -> dict:
        if not Product.validate_price(price):
            return {"error": "Product price must be a positive number"}

        existing_product = self.product_repository.get_product_by_id(product_id)
        if not existing_product:
            return {"error": "Product not found"}

        # Ensure only admin can update products; placeholder check
        if not self._is_admin():
            return {"error": "Only admin can update product details"}
        
        description = description if description else existing_product['description']

        product = Product(id=product_id, name=name, description=description, price=price, category_id=category_id)
        success = self.product_repository.update_product(product)
        if not success:
            return {"error": "Failed to update product"}

        return {"message": "Product updated successfully"}

    def _is_admin(self) -> bool:
        # Placeholder for actual admin check; can be replaced with real authentication logic
        return True