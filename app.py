# Epic Title: Delete Product

import logging
from backend.products.repositories.product_repository import ProductRepository
from backend.products.services.product_service import ProductService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    product_repository = ProductRepository()
    product_service = ProductService(product_repository=product_repository)

    try:
        # Example to delete an existing product
        product_service.delete_product("Test Product")
        logger.info("Product deleted successfully")

    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()