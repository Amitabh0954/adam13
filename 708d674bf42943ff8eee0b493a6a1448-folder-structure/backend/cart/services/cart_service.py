# Epic Title: Save Shopping Cart for Logged-in Users

from cart.repositories.cart_repository import CartRepository
from catalog.models.product import Product
from django.contrib.auth.models import User
from typing import Optional

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def get_or_create_cart(self, user: Optional[User] = None, session_id: Optional[str] = None) -> Cart:
        cart = None
        if user:
            cart = self.cart_repository.get_cart_by_user(user)
            if not cart:
                cart = self.cart_repository.create_cart_for_user(user)
        elif session_id:
            cart = self.cart_repository.get_cart_by_session_id(session_id)
            if not cart:
                cart = self.cart_repository.create_cart_for_session(session_id)
        return cart

    def add_product_to_cart(self, cart: Cart, product: Product, quantity: int) -> CartItem:
        return self.cart_repository.add_product_to_cart(cart, product, quantity)

    def remove_product_from_cart(self, cart_item_id: int) -> bool:
        return self.cart_repository.remove_product_from_cart(cart_item_id)

    def modify_quantity_in_cart(self, cart_item_id: int, quantity: int) -> bool:
        return self.cart_repository.modify_quantity_in_cart(cart_item_id, quantity)

    def save_cart_state(self, user: User) -> bool:
        cart = self.get_or_create_cart(user=user)
        if cart:
            cart_items = self.cart_repository.get_cart_items(cart)
            # Here we would persist the cart state to the user's profile
            # This is a simplified example assuming we save the cart state in the database.
            user.profile.saved_cart_state = [{
                "product_id": item.product.id,
                "quantity": item.quantity
            } for item in cart_items]
            user.profile.save()
            return True
        return False