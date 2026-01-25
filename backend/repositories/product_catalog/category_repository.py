from sqlalchemy.orm import Session
from .models.category import Category

class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_category(self, category: Category):
        self.session.add(category)
        self.session.commit()
        return category

    def get_category_by_name(self, name: str) -> Category:
        return self.session.query(Category).filter_by(name=name).first()

    def get_all_categories(self):
        return self.session.query(Category).all()