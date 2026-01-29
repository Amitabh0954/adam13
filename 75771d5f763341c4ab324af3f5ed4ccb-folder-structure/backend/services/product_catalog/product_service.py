# Epic Title: Add New Product

from repositories.product_catalog.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, data: dict) -> dict:
        product_data = {
            'name': data['name'],
            'price': data['price'],
            'description': data['description']
        }
        product_id = self.product_repository.save_product(product_data)
        return {"msg": "Product added successfully", "product_id": product_id}