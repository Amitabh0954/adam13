# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.product_catalog_management.models.product import Product

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return db_session.query(Product).filter_by(name=name).first()

    def get_product_by_id(self, product_id: int) -> Product:
        return db_session.query(Product).filter_by(id=product_id).first()
    
    def add_product(self, name: str, description: str, price: float, category_id: int):
        new_product = Product(name=name, description=description, price=price, category_id=category_id)
        db_session.add(new_product)
        db_session.commit()

    def update_product(self, product: Product):
        db_session.add(product)
        db_session.commit()