# Epic Title: Shopping Cart Functionality

from backend.database import db_session
from backend.models.cart import Cart, CartItem

class CartRepository:
    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        if not cart:
            cart = Cart(user_id=user_id)
            db_session.add(cart)
            db_session.commit()
        
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)

        db_session.add(cart_item)
        db_session.commit()

    def get_cart(self, user_id: int) -> Dict[str, Any]:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        if not cart:
            return {}

        return {
            'cart_id': cart.id,
            'user_id': cart.user_id,
            'items': [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart.items],
            'total_price': sum(item.quantity * item.product.price for item in cart.items)  # total price calculation
        }

    def remove_from_cart(self, user_id: int, product_id: int):
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        if not cart:
            return
        
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            db_session.delete(cart_item)
            db_session.commit()

    def update_quantity(self, user_id: int, product_id: int, quantity: int):
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        if not cart:
            return

        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            if quantity > 0:
                cart_item.quantity = quantity
                db_session.add(cart_item)
                db_session.commit()
            else:
                db_session.delete(cart_item)
                db_session.commit()