# Epic Title: Shopping Cart Functionality

from typing import Optional
from sqlalchemy.orm import Session
from backend.shopping_cart_functionality.models.cart import Cart
from backend.shopping_cart_functionality.models.cart_item import CartItem

class CartRepository:
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def find_cart_by_user_id(self, user_id: int) -> Optional[Cart]:
        return self.session.query(Cart).filter_by(user_id=user_id).first()
    
    def find_cart_by_session_id(self, session_id: str) -> Optional[Cart]:
        return self.session.query(Cart).filter_by(session_id=session_id).first()

    def add_item_to_cart(self, cart: Cart, product_id: int, quantity: int) -> CartItem:
        item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        self.session.add(item)
        self.session.commit()
        return item

    def remove_item_from_cart(self, cart: Cart, product_id: int) -> None:
        item = self.session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if item:
            self.session.delete(item)
            self.session.commit()

    def modify_item_quantity(self, cart: Cart, product_id: int, quantity: int) -> None:
        item = self.session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if item:
            item.quantity = quantity
            self.session.commit()

    def create_cart_for_user(self, user_id: int) -> Cart:
        cart = Cart(user_id=user_id)
        self.session.add(cart)
        self.session.commit()
        return cart
    
    def create_cart_for_session(self, session_id: str) -> Cart:
        cart = Cart(session_id=session_id)
        self.session.add(cart)
        self.session.commit()
        return cart