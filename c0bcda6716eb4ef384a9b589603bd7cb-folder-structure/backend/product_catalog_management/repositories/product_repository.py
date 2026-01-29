# Epic Title: Product Catalog Management

from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from backend.product_catalog_management.models.product import Product

class ProductRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_product(self, product: Product) -> None:
        self.session.add(product)
        self.session.commit()

    def find_by_name(self, name: str) -> Optional[Product]:
        return self.session.query(Product).filter_by(name=name).first()
    
    def find_by_id(self, product_id: int) -> Optional[Product]:
        return self.session.query(Product).filter_by(id=product_id).first()

    def update_product(self, product: Product) -> None:
        self.session.commit()

    def delete_product(self, product: Product) -> None:
        self.session.delete(product)
        self.session.commit()
    
    def search(self, query: str, page: int, per_page: int) -> List[Product]:
        offset = (page - 1) * per_page
        search_query = f"%{query}%"
        return self.session.query(Product).filter(
            (Product.name.ilike(search_query)) |
            (Product.description.ilike(search_query))
        ).offset(offset).limit(per_page).all()