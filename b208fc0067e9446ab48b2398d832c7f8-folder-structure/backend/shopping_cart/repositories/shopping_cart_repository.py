# Epic Title: Save Shopping Cart for Logged-in Users

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

    def remove_product_from_cart(self, cart: ShoppingCart, product: Product) -> None:
        try:
            cart_item = ShoppingCartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
        except ShoppingCartItem.DoesNotExist:
            pass

    def modify_product_quantity(self, cart: ShoppingCart, product: Product, quantity: int) -> Optional[ShoppingCartItem]:
        try:
            cart_item = ShoppingCartItem.objects.get(cart=cart, product=product)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
                return cart_item
            else:
                cart_item.delete()
                return None
        except ShoppingCartItem.DoesNotExist:
            return None

    def transfer_cart(self, session_cart: ShoppingCart, user_cart: ShoppingCart):
        """Transfer items from session-based cart to user-based cart."""
        for item in session_cart.items.all():
            self.add_product_to_cart(user_cart, item.product, item.quantity)
        session_cart.delete()