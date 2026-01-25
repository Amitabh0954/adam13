import logging
from backend.models.cart import Cart, CartItem
from backend.models.product import Product
from backend.database import db

logger = logging.getLogger(__name__)

class CartRepository:

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> CartItem:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            cart = Cart(user_id=user_id)
            db.session.add(cart)
            db.session.commit()

        product = Product.query.get(product_id)
        if not product:
            raise ValueError("Product not found")

        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        logger.info(f"Product '{product.name}' added to cart for user ID '{user_id}'")
        return cart_item

    def get_cart(self, user_id: int) -> list[CartItem]:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            raise ValueError("Cart not found for user")

        return cart.items

    def remove_from_cart(self, user_id: int, cart_item_id: int):
        cart_item = CartItem.query.get(cart_item_id)
        if not cart_item or cart_item.cart.user_id != user_id:
            raise ValueError("Cart item not found for user")
        
        db.session.delete(cart_item)
        db.session.commit()
        logger.info(f"Cart item with ID '{cart_item_id}' removed for user '{user_id}'")

    def update_cart_item_quantity(self, user_id: int, cart_item_id: int, quantity: int) -> CartItem:
        cart_item = CartItem.query.get(cart_item_id)
        if not cart_item or cart_item.cart.user_id != user_id:
            raise ValueError("Cart item not found for user")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        cart_item.quantity = quantity
        db.session.commit()
        logger.info(f"Quantity for cart item ID '{cart_item_id}' updated to '{quantity}'")
        return cart_item