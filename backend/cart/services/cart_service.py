# Epic Title: Modify Quantity of Products in Shopping Cart

from backend.cart.repositories.cart_repository import CartRepository
from backend.products.repositories.product_repository import ProductRepository
from backend.accounts.models.user import User
from backend.products.models.product import Product
from backend.cart.models.cart import Cart, CartItem
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class CartService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository) -> None:
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def add_to_cart(self, user: Optional[User], session_id: Optional[str], product_name: str, quantity: int) -> CartItem:
        cart = self.cart_repository.get_cart(user=user, session_id=session_id)
        if not cart:
            cart = self.cart_repository.create_cart(user=user, session_id=session_id)

        product = self.product_repository.get_product_by_name(product_name)
        if not product:
            raise ValueError("Product not found")

        cart_item = self.cart_repository.add_product(cart, product, quantity)
        logger.info(f"Added {quantity} of {product_name} to cart {cart.id}")
        return cart_item

    def remove_from_cart(self, user: Optional[User], session_id: Optional[str], product_name: str) -> None:
        cart = self.cart_repository.get_cart(user=user, session_id=session_id)
        if not cart:
            raise ValueError("Cart not found")

        product = self.product_repository.get_product_by_name(product_name)
        if not product:
            raise ValueError("Product not found")

        self.cart_repository.remove_product(cart, product)
        logger.info(f"Removed {product_name} from cart {cart.id}")

    def modify_quantity(self, user: Optional[User], session_id: Optional[str], product_name: str, new_quantity: int) -> CartItem:
        cart = self.cart_repository.get_cart(user=user, session_id=session_id)
        if not cart:
            raise ValueError("Cart not found")

        product = self.product_repository.get_product_by_name(product_name)
        if not product:
            raise ValueError("Product not found")

        cart_item = self.cart_repository.modify_product_quantity(cart, product, new_quantity)
        logger.info(f"Updated quantity of {product_name} to {new_quantity} in cart {cart.id}")
        return cart_item

    def get_cart_items(self, user: Optional[User], session_id: Optional[str]) -> Optional[Cart]:
        cart = self.cart_repository.get_cart(user=user, session_id=session_id)
        if not cart:
            raise ValueError("Cart not found")

        logger.info(f"Retrieved items for cart {cart.id}")
        return cart