# Epic Title: Save Shopping Cart for Logged-in Users

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

    def remove_item_from_cart(self, cart: Cart, product_id: int) -> bool:
        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            return True
        except CartItem.DoesNotExist:
            return False

    def update_item_quantity(self, cart: Cart, product_id: int, quantity: int) -> bool:
        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
                return True
            else:
                cart_item.delete()
                return True
        except CartItem.DoesNotExist:
            return False

    def save_cart_state(self, cart: Cart) -> None:
        cart.save()

    def retrieve_cart_state(self, user_id: int) -> Optional[Cart]:
        return self.get_cart_by_user(user_id)