from sqlalchemy.orm import Session
from .models.shopping_cart import ShoppingCart
from .models.shopping_cart_item import ShoppingCartItem

class ShoppingCartRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_cart_by_user_id(self, user_id: int) -> ShoppingCart:
        return self.session.query(ShoppingCart).filter_by(user_id=user_id).first()

    def get_cart_by_session_id(self, session_id: str) -> ShoppingCart:
        return self.session.query(ShoppingCart).filter_by(session_id=session_id).first()

    def add_cart(self, cart: ShoppingCart):
        self.session.add(cart)
        self.session.commit()
        return cart

    def add_item_to_cart(self, cart_item: ShoppingCartItem):
        self.session.add(cart_item)
        self.session.commit()
        return cart_item

    def remove_item_from_cart(self, cart_id: int, product_id: int):
        item = self.session.query(ShoppingCartItem).filter_by(cart_id=cart_id, product_id=product_id).first()
        if item:
            self.session.delete(item)
            self.session.commit()

#### 3. Implement services for removing products from the shopping cart