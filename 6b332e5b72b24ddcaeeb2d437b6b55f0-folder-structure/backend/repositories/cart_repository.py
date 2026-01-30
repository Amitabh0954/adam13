# Epic Title: Add Product to Shopping Cart

from backend.models.cart import Cart, CartItem
from backend.models.product import Product
from typing import Optional

class CartRepository:

    def get_cart_by_user(self, user_id: int) -> Optional[Cart]:
        try:
            return Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return None

    def get_cart_by_session_key(self, session_key: str) -> Optional[Cart]:
        try:
            return Cart.objects.get(session_key=session_key)
        except Cart.DoesNotExist:
            return None

    def add_item_to_cart(self, cart: Cart, product_id: int, quantity: int = 1) -> CartItem:
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()
        return cart_item