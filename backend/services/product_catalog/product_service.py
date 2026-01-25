from sqlalchemy.orm import Session
from backend.repositories.product_catalog.product_repository import ProductRepository
from backend.repositories.product_catalog.models.product import Product
from typing import List, Dict

class ProductService:
    def __init__(self, session: Session):
        self.product_repository = ProductRepository(session)

    def search_products(self, search_term: str, page: int = 1, page_size: int = 10) -> List[Dict]:
        products = self.product_repository.search_products(search_term, page, page_size)
        results = []
        for product in products:
            highlighted_name = product.name.replace(search_term, f"<mark>{search_term}</mark>")
            highlighted_category = product.category.replace(search_term, f"<mark>{search_term}</mark>")
            highlighted_attributes = product.attributes.replace(search_term, f"<mark>{search_term}</mark>")
            results.append({
                "id": product.id,
                "name": highlighted_name,
                "category": highlighted_category,
                "attributes": highlighted_attributes,
                "description": product.description,
                "price": product.price
            })
        return results

#### 4. Implement a controller to expose the API for searching products