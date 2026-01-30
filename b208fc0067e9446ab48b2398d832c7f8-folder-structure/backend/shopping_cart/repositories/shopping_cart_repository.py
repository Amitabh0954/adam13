# Epic Title: Add Product to Shopping Cart

from shopping_cart.models.shopping_cart import ShoppingCart, ShoppingCartItem
from product_catalog_management.models.product import Product
from user_account_management.models.user import User
from django.contrib.sessions.models import Session
from typing import Optional

class ShoppingCartRepository:

    def get_or_create_cart(self, user: Optional[User], session: Optional[Session]) -> ShoppingCart:
        if user:
            cart, created = ShoppingCart.objects.get_or_create(user=user)
        else:
            cart, created = ShoppingCart.objects.get_or_create(session=session)
        return cart

    def add_product_to_cart(self, cart: ShoppingCart, product: Product, quantity: int) -> ShoppingCartItem:
        cart_item, created = ShoppingCartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()
        return cart_item

    def get_cart_items(self, cart: ShoppingCart):
        return cart.items.all()