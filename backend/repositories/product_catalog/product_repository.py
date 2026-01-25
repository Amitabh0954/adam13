from sqlalchemy.orm import Session
from .models.product import Product

class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_product(self, product: Product):
        self.session.add(product)
        self.session.commit()
        return product

    def get_product_by_name(self, name: str) -> Product:
        return self.session.query(Product).filter_by(name=name).first()

#### 3. Implement services for adding new products ensuring all constraints