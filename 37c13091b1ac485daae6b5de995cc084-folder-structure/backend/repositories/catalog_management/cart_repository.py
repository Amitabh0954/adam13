from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from backend.extensions import db

class CartRepository:
    # Inline comment referencing the Epic Title
    # Epic Title: Shopping Cart Functionality

    def find_cart_by_user_id(self, user_id: int) -> Cart:
        return Cart.query.filter_by(user_id=user_id).first()

    def create_cart(self, user_id: int) -> Cart:
        new_cart = Cart(user_id=user_id)
        db.session.add(new_cart)
        db.session.commit()
        return new_cart

    def add_to_cart(self, cart: Cart, product_id: int, quantity: int):
        existing_item = next((item for item in cart.items if item.product_id == product_id), None)
        if existing_item:
            existing_item.quantity += quantity
        else:
            new_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            cart.items.append(new_item)
        db.session.commit()