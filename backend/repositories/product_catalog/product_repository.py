from sqlalchemy.orm import Session
from sqlalchemy import or_
from .models.product import Product

class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_product(self, product: Product):
        self.session.add(product)
        self.session.commit()
        return product

    def get_product_by_name(self, name: str) -> Product:
        return self.session.query(Product).filter_by(name=name, is_deleted=False).first()

    def search_products(self, search_term: str, page: int = 1, page_size: int = 10):
        query = self.session.query(Product)\
            .filter(
                Product.is_deleted == False,
                or_(
                    Product.name.like(f"%{search_term}%"),
                    Product.category.like(f"%{search_term}%"),
                    Product.attributes.like(f"%{search_term}%")
                )
            )\
            .offset((page - 1) * page_size)\
            .limit(page_size)
        return query.all()

#### 3. Implement services for searching products ensuring all constraints