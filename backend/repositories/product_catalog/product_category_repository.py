from sqlalchemy.orm import Session
from .models.product_category import ProductCategory

class ProductCategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_product_category(self, product_category: ProductCategory):
        self.session.add(product_category)
        self.session.commit()
        return product_category

    def get_product_categories(self, product_id: int):
        return self.session.query(ProductCategory).filter_by(product_id=product_id).all()

#### 4. Implement services for managing categories and associating products with categories