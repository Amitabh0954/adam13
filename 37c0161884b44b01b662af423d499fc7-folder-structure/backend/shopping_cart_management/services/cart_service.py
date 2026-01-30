# Epic Title: Save Shopping Cart for Logged-in Users

from typing import Optional
from shopping_cart_management.repositories.cart_repository import CartRepository
from user_account_management.models.user import User
from product_catalog_management.models.product import Product
from shopping_cart_management.models.shopping_cart import ShoppingCart, ShoppingCartItem

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_product_to_cart(self, user: User, product: Product, quantity: int = 1) -> Optional[ShoppingCartItem]:
        cart = self.cart_repository.get_cart_by_user(user)
        if not cart:
            cart = self.cart_repository.create_cart(user)
        return self.cart_repository.add_product_to_cart(cart, product, quantity)

    def remove_product_from_cart(self, user: User, product: Product) -> bool:
        cart = self.cart_repository.get_cart_by_user(user)
        if cart:
            return self.cart_repository.remove_product_from_cart(cart, product)
        return False

    def modify_product_quantity(self, user: User, product: Product, quantity: int) -> Optional[ShoppingCartItem]:
        cart = self.cart_repository.get_cart_by_user(user)
        if cart:
            if quantity <= 0:
                self.cart_repository.remove_product_from_cart(cart, product)
                return None
            else:
                return self.cart_repository.update_product_quantity(cart, product, quantity)
        return None

    def get_cart(self, user: User) -> Optional[ShoppingCart]:
        return self.cart_repository.get_cart_by_user(user)