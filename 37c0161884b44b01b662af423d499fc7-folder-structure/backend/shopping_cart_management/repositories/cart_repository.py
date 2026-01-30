# Epic Title: Save Shopping Cart for Logged-in Users

from typing import Optional
from shopping_cart_management.models.shopping_cart import ShoppingCart, ShoppingCartItem
from user_account_management.models.user import User
from product_catalog_management.models.product import Product

class CartRepository:

    def get_cart_by_user(self, user: User) -> Optional[ShoppingCart]:
        try:
            return ShoppingCart.objects.get(user=user)
        except ShoppingCart.DoesNotExist:
            return None

    def create_cart(self, user: User) -> ShoppingCart:
        cart = ShoppingCart(user=user)
        cart.save()
        return cart

    def add_product_to_cart(self, cart: ShoppingCart, product: Product, quantity: int = 1) -> ShoppingCartItem:
        item, created = ShoppingCartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        item.save()
        return item

    def remove_product_from_cart(self, cart: ShoppingCart, product: Product) -> bool:
        try:
            item = ShoppingCartItem.objects.get(cart=cart, product=product)
            item.delete()
            return True
        except ShoppingCartItem.DoesNotExist:
            return False

    def update_product_quantity(self, cart: ShoppingCart, product: Product, quantity: int) -> Optional[ShoppingCartItem]:
        try:
            item = ShoppingCartItem.objects.get(cart=cart, product=product)
            item.quantity = quantity
            item.save()
            return item
        except ShoppingCartItem.DoesNotExist:
            return None