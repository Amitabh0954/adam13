import logging
from backend.models.product import Product, Category
from backend.database import db

logger = logging.getLogger(__name__)

class ProductSearchRepository:

    def search_products(self, search_term: str, page: int, per_page: int):
        query = (
            Product.query.join(Category)
            .filter(
                db.or_(
                    Product.name.like(f"%{search_term}%"),
                    Product.description.like(f"%{search_term}%"),
                    Category.name.like(f"%{search_term}%")
                )
            )
        )
        results = query.paginate(page, per_page, False).items
        logger.info(f"Search query found {len(results)} products for term '{search_term}'")
        return results