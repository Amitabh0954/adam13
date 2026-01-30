# Epic Title: Add Product to Shopping Cart

from cart.repositories.cart_repository import CartRepository
from catalog.models.product import Product
from django.contrib.auth.models import User
from typing import Optional

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def get_or_create_cart(self, user: Optional[User] = None, session_id: Optional[str] = None):
        if user:
            cart = self.cart_repository.get_cart_by_user(user)
            if not cart:
                cart = self.cart_repository.create_cart_for_user(user)
        else:
            cart = self.cart_repository.get_cart_by_session_id(session_id)
            if not cart:
                cart = self.cart_repository.create_cart_for_session(session_id)
        return cart

    def add_product_to_cart(self, cart, product: Product, quantity: int):
        return self.cart_repository.add_product_to_cart(cart, product, quantity)