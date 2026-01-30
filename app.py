# Epic Title: Save Shopping Cart for Logged-in Users

import logging
from backend.products.repositories.product_repository import ProductRepository
from backend.cart.repositories.cart_repository import CartRepository
from backend.cart.services.cart_service import CartService
from backend.accounts.models.user import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    product_repository = ProductRepository()
    cart_repository = CartRepository()
    cart_service = CartService(cart_repository=cart_repository, product_repository=product_repository)

    session_id = "sample-session-id"
    user = User.objects.get(username="testuser")  # assuming a user with username "testuser" exists

    try:
        # Add product to session cart
        cart_service.add_to_cart(user=None, session_id=session_id, product_name="iPhone 13", quantity=1)

        # Save session cart state to user profile
        cart_service.save_cart_state(user=user, session_id=session_id)

        # List cart items for the user
        cart = cart_service.get_cart_items(user=user, session_id=None)
        for item in cart.items.all():
            logger.info(f"Cart item: {item.quantity} of {item.product.name}")
        logger.info(f"Total cart price: {cart.total_price}")

    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()