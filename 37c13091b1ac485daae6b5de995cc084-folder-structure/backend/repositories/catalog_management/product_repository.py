from backend.models.product import Product
from backend.extensions import db

class ProductRepository:
    def find_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()
    
    def save_product(self, product: Product):
        db.session.add(product)
        db.session.commit()