from backend.products.models.product import Product
from backend.auth.extensions import db

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.filter_by(id=product_id).first()

    def create_product(self, name: str, price: float, description: str) -> Product:
        new_product = Product(name=name, price=price, description=description)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    def update_product(self, product: Product) -> Product:
        db.session.commit()
        return product
    
    def delete_product(self, product_id: int):
        product = self.get_product_by_id(product_id)
        if product:
            product.is_active = False
            db.session.commit()