from sqlalchemy.orm import Session
from backend.repositories.product_catalog.category_repository import CategoryRepository
from backend.repositories.product_catalog.models.category import Category
from marshmallow import ValidationError
from .schemas.category_schema import CategorySchema

class CategoryService:
    def __init__(self, session: Session):
        self.category_repository = CategoryRepository(session)

    def add_category(self, data: dict) -> Category:
        try:
            valid_data = CategorySchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        if self.category_repository.get_category_by_name(valid_data['name']):
            raise ValueError("Category name already exists")

        category = Category(
            name=valid_data['name'],
            parent_id=valid_data.get('parent_id')
        )

        return self.category_repository.add_category(category)

    def get_all_categories(self):
        return self.category_repository.get_all_categories()