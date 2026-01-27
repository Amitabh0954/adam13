# Epic Title: Shopping Cart Functionality

from backend.database import db_session
from backend.models.cart import Cart, CartItem
from typing import Optional

class CartRepository:
    def get_cart_by_user(self, user_id: int) -> Optional[Cart]:
        return db_session.query(Cart).filter_by(user_id=user_id).first()

    def get_cart_by_session(self) -> Optional[Cart]:
        return db_session.query(Cart).filter_by(user_id=None).first()

    def create_cart(self, user_id: Optional[int]) -> Cart:
        new_cart = Cart(user_id=user_id)
        db_session.add(new_cart)
        db_session.commit()
        return new_cart

    def add_product_to_cart(self, cart: Cart, product_id: int, quantity: int):
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            db_session.add(cart_item)
        db_session.commit()

    def remove_product_from_cart(self, cart: Cart, product_id: int):
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            db_session.delete(cart_item)
            db_session.commit()

    def update_product_quantity(self, cart: Cart, product_id: int, quantity: int):
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity = quantity
            db_session.commit()

    def save_cart(self, user_id: int):
        cart = self.get_cart_by_user(user_id)
        db_session.commit()

    def load_cart(self, user_id: int) -> Optional[Cart]:
        return self.get_cart_by_user(user_id)