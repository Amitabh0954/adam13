from sqlalchemy.orm import Session
from backend.repositories.product_catalog.product_repository import ProductRepository
from backend.repositories.product_catalog.models.product import Product
from marshmallow import ValidationError
from .schemas.product_schema import ProductSchema

class ProductService:
    def __init__(self, session: Session):
        self.product_repository = ProductRepository(session)

    def add_product(self, data: dict) -> Product:
        try:
            valid_data = ProductSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        if self.product_repository.get_product_by_name(valid_data['name']):
            raise ValueError("Product name already exists")

        product = Product(
            name=valid_data['name'],
            description=valid_data['description'],
            price=valid_data['price']
        )

        return self.product_repository.add_product(product)

##### Product Schema