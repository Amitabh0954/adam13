import logging
from backend.models.product import Product
from backend.database import db
from sqlalchemy import or_

logger = logging.getLogger(__name__)

class SearchProductRepository:
    
    def search_products(self, query: str, page: int, per_page: int):
        search_query = "%{}%".format(query)
        products = Product.query.filter(
            or_(
                Product.name.like(search_query),
                Product.description.like(search_query),
                Product.category.like(search_query)
            )
        ).paginate(page=page, per_page=per_page, error_out=False)
        
        logger.info(f"Found {products.total} products for query: {query}")
        return products