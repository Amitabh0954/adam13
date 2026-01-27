from backend.models.product import Product
from backend.extensions import db

class ProductRepository:
    def find_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()
    
    def find_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)
    
    def save_product(self, product: Product):
        db.session.add(product)
        db.session.commit()

    def update_product(self, product: Product):
        db.session.commit()