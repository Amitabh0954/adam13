# Epic Title: Shopping Cart Functionality

from backend.database import db_session
from backend.models.product import Product

class ProductRepository:
    def get_product_by_id(self, product_id: int) -> Product:
        return db_session.query(Product).filter_by(id=product_id).first()

    def get_product_by_name(self, name: str) -> Product:
        return db_session.query(Product).filter_by(name=name).first()

    def create_product(self, name: str, description: str, price: float) -> Product:
        new_product = Product(name=name, description=description, price=price)
        db_session.add(new_product)
        db_session.commit()
        return new_product

    def update_product(self, product: Product):
        db_session.add(product)
        db_session.commit()

    def delete_product(self, product: Product):
        db_session.delete(product)
        db_session.commit()

    def search_products(self, query: str, page: int, per_page: int):
        offset = (page - 1) * per_page
        products = db_session.query(Product).filter(
            or_(
                Product.name.like(f'%{query}%'),
                Product.description.like(f'%{query}%')
            )
        ).offset(offset).limit(per_page).all()
        return products

    def count_search_results(self, query: str) -> int:
        count = db_session.query(Product).filter(
            or_(
                Product.name.like(f'%{query}%'),
                Product.description.like(f'%{query}%')
            )
        ).count()
        return count