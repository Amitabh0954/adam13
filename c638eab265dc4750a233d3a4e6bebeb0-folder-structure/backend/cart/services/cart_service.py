# Epic Title: Add Product to Shopping Cart

from cart.repositories.cart_repository import CartRepository
from cart.models.cart import Cart, CartItem
from products.models.product import Product
from django.contrib.auth.models import User
from typing import Optional

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def get_or_create_cart(self, user: Optional[User]) -> Cart:
        cart = self.cart_repository.get_cart_by_user(user)
        if not cart:
            cart = self.cart_repository.create_cart(user)
        return cart

    def add_product_to_cart(self, user: Optional[User], product_id: int, quantity: int) -> Optional[CartItem]:
        cart = self.get_or_create_cart(user)
        product = Product.objects.get(id=product_id)
        return self.cart_repository.add_cart_item(cart, product, quantity)

    def get_cart_items(self, user: Optional[User]) -> Cart:
        cart = self.get_or_create_cart(user)
        return self.cart_repository.get_cart_items(cart)