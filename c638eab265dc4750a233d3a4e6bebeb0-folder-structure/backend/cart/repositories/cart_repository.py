# Epic Title: Modify Quantity of Products in Shopping Cart

from cart.models.cart import Cart, CartItem
from products.models.product import Product
from django.contrib.auth.models import User
from typing import Optional

class CartRepository:

    def create_cart(self, user: Optional[User]) -> Cart:
        cart = Cart(user=user)
        cart.save()
        return cart

    def get_cart_by_user(self, user: User) -> Optional[Cart]:
        try:
            return Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return None

    def get_cart_item(self, cart: Cart, product: Product) -> Optional[CartItem]:
        try:
            return CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            return None

    def add_cart_item(self, cart: Cart, product: Product, quantity: int) -> CartItem:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item

    def remove_cart_item(self, cart: Cart, product: Product) -> bool:
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
            return True
        except CartItem.DoesNotExist:
            return False

    def update_cart_item_quantity(self, cart: Cart, product: Product, quantity: int) -> bool:
        cart_item = self.get_cart_item(cart, product)
        if cart_item:
            cart_item.quantity = quantity
            cart_item.save()
            return True
        return False

    def get_cart_items(self, cart: Cart) -> Cart:
        return cart.items.all()