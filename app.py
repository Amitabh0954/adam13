# Epic Title: Update Product Details

import logging
from backend.products.repositories.product_repository import ProductRepository
from backend.products.services.product_service import ProductService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    product_repository = ProductRepository()
    product_service = ProductService(product_repository=product_repository)

    try:
        # Example to update an existing product
        updated_product = product_service.update_product(
            "Test Product",
            "This is the updated test product description.",
            79.99
        )
        logger.info(f"Product updated: {updated_product.name}")

    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()