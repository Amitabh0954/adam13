import logging
from backend.models.cart import Cart, CartItem
from backend.database import db

logger = logging.getLogger(__name__)

class CartRepository:
    
    def get_cart(self, user_id: int) -> Cart:
        return Cart.query.filter_by(user_id=user_id).first()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> Cart:
        cart = self.get_cart(user_id)
        if not cart:
            cart = Cart(user_id=user_id)
            db.session.add(cart)
            db.session.commit()
        
        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)
        
        db.session.commit()
        return cart

    def remove_from_cart(self, user_id: int, product_id: int) -> Cart:
        cart = self.get_cart(user_id)
        if not cart:
            raise ValueError("Cart not found")
        
        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
        if not cart_item:
            raise ValueError("Product not in cart")
        
        db.session.delete(cart_item)
        db.session.commit()
        return cart

    def modify_cart_item(self, user_id: int, product_id: int, quantity: int) -> Cart:
        cart = self.get_cart(user_id)
        if not cart:
            raise ValueError("Cart not found")
        
        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
        if not cart_item:
            raise ValueError("Product not in cart")
        
        cart_item.quantity = quantity
        db.session.commit()
        return cart