from sqlalchemy.orm import Session
from backend.repositories.product_catalog.product_category_repository import ProductCategoryRepository
from backend.repositories.product_catalog.models.product_category import ProductCategory
from marshmallow import ValidationError
from .schemas.product_category_schema import ProductCategorySchema

class ProductCategoryService:
    def __init__(self, session: Session):
        self.product_category_repository = ProductCategoryRepository(session)

    def add_product_category(self, data: dict) -> ProductCategory:
        try:
            valid_data = ProductCategorySchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        product_category = ProductCategory(
            product_id=valid_data['product_id'],
            category_id=valid_data['category_id']
        )

        return self.product_category_repository.add_product_category(product_category)

    def get_product_categories(self, product_id: int):
        return self.product_category_repository.get_product_categories(product_id)

##### Category Schema