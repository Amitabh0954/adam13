# Epic Title: Product Catalog Management

from typing import Optional
from sqlalchemy.orm import Session
from backend.product_catalog_management.models.product import Product

class ProductRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_product(self, product: Product) -> None:
        self.session.add(product)
        self.session.commit()

    def find_by_name(self, name: str) -> Optional[Product]:
        return self.session.query(Product).filter_by(name=name).first()