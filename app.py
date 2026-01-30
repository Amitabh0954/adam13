# Epic Title: Remove Product from Shopping Cart

import logging
from backend.products.repositories.product_repository import ProductRepository
from backend.cart.repositories.cart_repository import CartRepository
from backend.cart.services.cart_service import CartService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    product_repository = ProductRepository()
    cart_repository = CartRepository()
    cart_service = CartService(cart_repository=cart_repository, product_repository=product_repository)

    session_id = "sample-session-id"

    try:
        # Add product to cart
        cart_service.add_to_cart(user=None, session_id=session_id, product_name="iPhone 13", quantity=1)

        # Remove product from cart with confirmation
        if input("Are you sure you want to remove the product from the cart? (yes/no): ").strip().lower() == "yes":
            cart_service.remove_from_cart(user=None, session_id=session_id, product_name="iPhone 13")
            logger.info("Product removed from cart")

        # List cart items
        cart = cart_service.get_cart_items(user=None, session_id=session_id)
        for item in cart.items.all():
            logger.info(f"Cart item: {item.quantity} of {item.product.name}")
        logger.info(f"Total cart price: {cart.total_price}")

    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()