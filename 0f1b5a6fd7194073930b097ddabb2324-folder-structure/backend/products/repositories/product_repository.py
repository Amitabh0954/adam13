from backend.products.models.product import Product
from backend.auth.extensions import db

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    def create_product(self, name: str, price: float, description: str) -> Product:
        new_product = Product(name=name, price=price, description=description)
        db.session.add(new_product)
        db.session.commit()
        return new_product