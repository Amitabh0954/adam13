# Epic Title: Product Catalog Management

from backend.database import db_session
from backend.models.product import Product
from sqlalchemy import or_

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return db_session.query(Product).filter_by(name=name).first()

    def add_product(self, name: str, price: float, description: str, category_id: int) -> Product:
        new_product = Product(name=name, price=price, description=description, category_id=category_id)
        db_session.add(new_product)
        db_session.commit()
        return new_product

    def get_product_by_id(self, product_id: int) -> Product:
        return db_session.query(Product).filter_by(id=product_id).first()

    def update_product(self, product: Product):
        db_session.add(product)
        db_session.commit()

    def delete_product(self, product: Product):
        db_session.delete(product)
        db_session.commit()

    def search_products(self, query: str, page: int, per_page: int) -> Dict:
        search_filter = or_(Product.name.ilike(f'%{query}%'), 
                            Product.description.ilike(f'%{query}%'), 
                            Product.category.has(Category.name.ilike(f'%{query}%')))

        total = db_session.query(Product).filter(search_filter).count()
        items = db_session.query(Product).filter(search_filter).offset((page - 1) * per_page).limit(per_page).all()

        return {
            'items': items,
            'total': total,
            'page': page,
            'per_page': per_page
        }