# Epic Title: Add Product to Shopping Cart

from backend.cart.models.cart import Cart, CartItem
from backend.products.models.product import Product
from typing import Optional

class CartRepository:
    def create_cart(self, user: Optional[User] = None, session_id: Optional[str] = None) -> Cart:
        cart = Cart(user=user, session_id=session_id)
        cart.save()
        return cart

    def get_cart(self, user: Optional[User] = None, session_id: Optional[str] = None) -> Optional[Cart]:
        if user:
            return Cart.objects.filter(user=user).first()
        elif session_id:
            return Cart.objects.filter(session_id=session_id).first()
        return None

    def add_product(self, cart: Cart, product: Product, quantity: int) -> CartItem:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()
        return cart_item

    def remove_product(self, cart: Cart, product: Product) -> None:
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            cart_item.delete()

    def clear_cart(self, cart: Cart) -> None:
        CartItem.objects.filter(cart=cart).delete()