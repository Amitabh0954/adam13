# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.models.product import Product
from sqlalchemy.orm import load_only

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return db_session.query(Product).filter_by(name=name).first()

    def get_product_by_id(self, product_id: int) -> Product:
        return db_session.query(Product).filter_by(id=product_id).first()

    def create_product(self, name: str, description: str, price: float, category_id: int) -> Product:
        new_product = Product(name=name, description=description, price=price, category_id=category_id)
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
        search_query = "%{}%".format(query)
        return db_session.query(Product).filter(
            Product.name.like(search_query) |
            Product.description.like(search_query) |
            Product.category.has(name=search_query)
        ).options(load_only('id', 'name', 'description', 'price', 'category_id')).paginate(page, per_page, False)