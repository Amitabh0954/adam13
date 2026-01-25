from sqlalchemy.orm import Session
from backend.repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository
from backend.repositories.shopping_cart.models.shopping_cart import ShoppingCart
from backend.repositories.shopping_cart.models.shopping_cart_item import ShoppingCartItem

class ShoppingCartService:
    def __init__(self, session: Session):
        self.shopping_cart_repository = ShoppingCartRepository(session)

    def add_product_to_cart(self, user_id: int, session_id: str, product_id: int, quantity: int, price: float):
        if user_id:
            cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
            if not cart:
                cart = ShoppingCart(user_id=user_id)
                self.shopping_cart_repository.add_cart(cart)
        else:
            cart = self.shopping_cart_repository.get_cart_by_session_id(session_id)
            if not cart:
                cart = ShoppingCart(session_id=session_id)
                self.shopping_cart_repository.add_cart(cart)

        cart_item = ShoppingCartItem(cart_id=cart.id, product_id=product_id, quantity=quantity, price=price)
        self.shopping_cart_repository.add_item_to_cart(cart_item)
        return cart_item

#### 4. Implement a controller to expose the API for managing the shopping cart