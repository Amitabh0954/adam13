# Epic Title: Modify Quantity of Products in Shopping Cart

from cart.repositories.cart_repository import CartRepository
from catalog.models.product import Product
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