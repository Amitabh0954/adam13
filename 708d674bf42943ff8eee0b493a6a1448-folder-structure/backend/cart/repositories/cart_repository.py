# Epic Title: Save Shopping Cart for Logged-in Users

from cart.models.cart import Cart, CartItem
from catalog.models.product import Product
from django.contrib.auth.models import User
from typing import Optional, List

class CartRepository:

    def get_cart_by_user(self, user: User) -> Optional[Cart]:
        return Cart.objects.filter(user=user).first()

    def get_cart_by_session_id(self, session_id: str) -> Optional[Cart]:
        return Cart.objects.filter(session_id=session_id).first()

    def create_cart_for_user(self, user: User) -> Cart:
        return Cart.objects.create(user=user)

    def create_cart_for_session(self, session_id: str) -> Cart:
        return Cart.objects.create(session_id=session_id)

    def add_product_to_cart(self, cart: Cart, product: Product, quantity: int) -> CartItem:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return cart_item

    def remove_product_from_cart(self, cart_item_id: int) -> bool:
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete()
            return True
        except CartItem.DoesNotExist:
            return False

    def modify_quantity_in_cart(self, cart_item_id: int, quantity: int) -> bool:
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.quantity = quantity
            cart_item.save()
            return True
        except CartItem.DoesNotExist:
            return False

    def get_cart_items(self, cart: Cart) -> List[CartItem]:
        return list(CartItem.objects.filter(cart=cart))