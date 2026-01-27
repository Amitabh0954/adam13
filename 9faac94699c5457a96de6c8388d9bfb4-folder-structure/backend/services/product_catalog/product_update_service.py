# Epic Title: Product Catalog Management

from backend.repositories.product_catalog.product_repository import ProductRepository

class ProductUpdateService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, name: str, description: str, price: float) -> dict:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {'status': 'error', 'message': 'Product not found'}

        if name:
            product.name = name
        if description:
            product.description = description
        if price is not None:
            product.price = price

        self.product_repository.update_product(product)
        return {'status': 'success', 'message': 'Product updated successfully'}