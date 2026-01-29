# Epic Title: Update Product Details

from repositories.product_catalog.product_repository import ProductRepository

class ProductUpdateService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def update_product(self, product_id: int, data: dict) -> dict:
        updated_data = {
            'name': data.get('name'),
            'price': data.get('price'),
            'description': data.get('description')
        }
        self.product_repository.update_product(product_id, updated_data)
        return {"msg": "Product updated successfully"}