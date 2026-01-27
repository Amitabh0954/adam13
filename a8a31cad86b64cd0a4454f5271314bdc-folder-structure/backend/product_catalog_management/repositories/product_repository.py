# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.product_catalog_management.models.product import Product

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return db_session.query(Product).filter_by(name=name).first()
    
    def add_product(self, name: str, description: str, price: float, category_id: int):
        new_product = Product(name=name, description=description, price=price, category_id=category_id)
        db_session.add(new_product)
        db_session.commit()