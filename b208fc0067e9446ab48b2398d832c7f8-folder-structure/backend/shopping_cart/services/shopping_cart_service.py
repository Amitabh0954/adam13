# Epic Title: Modify Quantity of Products in Shopping Cart

from shopping_cart.repositories.shopping_cart_repository import ShoppingCartRepository
from product_catalog_management.models.product import Product
from user_account_management.models.user import User
from django.contrib.sessions.models import Session
from typing import Optional

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_product_to_cart(self, user: Optional[User], session: Optional[Session], product: Product, quantity: int) -> None:
        cart = self.shopping_cart_repository.get_or_create_cart(user, session)
        self.shopping_cart_repository.add_product_to_cart(cart, product, quantity)

    def get_cart_items(self, user: Optional[User], session: Optional[Session]):
        cart = self.shopping_cart_repository.get_or_create_cart(user, session)
        return self.shopping_cart_repository.get_cart_items(cart)

    def remove_product_from_cart(self, user: Optional[User], session: Optional[Session], product: Product) -> None:
        cart = self.shopping_cart_repository.get_or_create_cart(user, session)
        self.shopping_cart_repository.remove_product_from_cart(cart, product)

    def modify_product_quantity(self, user: Optional[User], session: Optional[Session], product: Product, quantity: int) -> Optional[str]:
        cart = self.shopping_cart_repository.get_or_create_cart(user, session)
        if quantity <= 0:
            return "Quantity must be a positive integer"
        return self.shopping_cart_repository.modify_product_quantity(cart, product, quantity)