import logging
from backend.models.cart import Cart
from backend.database import db

logger = logging.getLogger(__name__)

class ShoppingCartRepository:
    
    def get_cart_by_user_id(self, user_id: int) -> Cart:
        return Cart.query.filter_by(user_id=user_id).first()
    
    def save_cart(self, cart: Cart) -> None:
        db.session.add(cart)
        db.session.commit()
        logger.info(f"Cart saved for user {cart.user_id}")