from backend.cart.models.cart import Cart, CartItem
from backend.auth.extensions import db

class CartRepository:
    def get_or_create_cart(self, user_id=None, session_id=None) -> Cart:
        cart = None
        if user_id:
            cart = Cart.query.filter_by(user_id=user_id).first()
        elif session_id:
            cart = Cart.query.filter_by(session_id=session_id).first()

        if not cart:
            cart = Cart(user_id=user_id, session_id=session_id)
            db.session.add(cart)
            db.session.commit()

        return cart

    def get_cart_by_user_id(self, user_id: int) -> Cart:
        return Cart.query.filter_by(user_id=user_id).first()

    def get_cart_by_session_id(self, session_id: str) -> Cart:
        return Cart.query.filter_by(session_id=session_id).first()

    def add_product_to_cart(self, cart_id: int, product_id: int, quantity: int) -> CartItem:
        cart_item = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)
        db.session.commit()
        return cart_item

    def remove_product_from_cart(self, cart_id: int, cart_item_id: int):
        cart_item = CartItem.query.filter_by(cart_id=cart_id, id=cart_item_id).first()
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
    
    def modify_cart_item_quantity(self, cart_id: int, cart_item_id: int, quantity: int) -> CartItem:
        cart_item = CartItem.query.filter_by(cart_id=cart_id, id=cart_item_id).first()
        if cart_item:
            cart_item.quantity = quantity
            db.session.commit()
        return cart_item