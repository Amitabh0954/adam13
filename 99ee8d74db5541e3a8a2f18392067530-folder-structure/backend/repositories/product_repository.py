# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.models.product import Product

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return db_session.query(Product).filter_by(name=name).first()

    def add_product(self, name: str, price: float, description: str, category_id: int) -> Product:
        new_product = Product(name=name, price=price, description=description, category_id=category_id)
        db_session.add(new_product)
        db_session.commit()
        return new_product