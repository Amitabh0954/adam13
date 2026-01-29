# Epic Title: Product Catalog Management

from typing import Optional, List
from sqlalchemy.orm import Session
from backend.product_catalog_management.models.category import Category

class CategoryRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_category(self, category: Category) -> None:
        self.session.add(category)
        self.session.commit()

    def find_by_name(self, name: str) -> Optional<Category]:
        return self.session.query(Category).filter_by(name=name).first()
    
    def find_by_id(self, category_id: int) -> Optional<Category]:
        return self.session.query(Category).filter_by(id=category_id).first()

    def update_category(self, category: Category) -> None:
        self.session.commit()

    def delete_category(self, category: Category) -> None:
        self.session.delete(category)
        self.session.commit()

    def list_all_categories(self) -> List[Category]:
        return self.session.query(Category).all()