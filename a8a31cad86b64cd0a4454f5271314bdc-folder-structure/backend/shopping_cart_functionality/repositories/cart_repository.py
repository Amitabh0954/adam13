# Epic Title: Shopping Cart Functionality

from backend.database import db_session
from backend.shopping_cart_functionality.models.cart import Cart
from typing import List

class CartRepository:
    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        cart_item = db_session.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)

        db_session.add(cart_item)
        db_session.commit()

    def remove_from_cart(self, user_id: int, product_id: int):
        cart_item = db_session.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            db_session.delete(cart_item)
            db_session.commit()
    
    def update_cart(self, user_id: int, product_id: int, quantity: int):
        cart_item = db_session.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity = quantity
            db_session.add(cart_item)
            db_session.commit()
    
    def get_cart_by_user(self, user_id: int) -> List[Cart]:
        return db_session.query(Cart).filter_by(user_id=user_id).all()