from sqlalchemy.orm import Session
from backend.repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository
from backend.repositories.shopping_cart.models.shopping_cart import ShoppingCart
from backend.repositories.shopping_cart.models.shopping_cart_item import ShoppingCartItem

class ShoppingCartService:
    def __init__(self, session: Session):
        self.shopping_cart_repository = ShoppingCartRepository(session)

    def save_shopping_cart(self, user_id: int, session_id: str):
        cart = self.shopping_cart_repository.get_cart_by_session_id(session_id)
        if not cart:
            raise ValueError("Shopping cart not found for the session")

        cart.user_id = user_id
        self.shopping_cart_repository.add_cart(cart)

    def retrieve_shopping_cart(self, user_id: int) -> ShoppingCart:
        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            raise ValueError("Shopping cart not found for the user")

        cart_items = self.shopping_cart_repository.get_cart_items(cart.id)
        return {"cart": cart, "items": cart_items}

#### 4. Implement a controller to expose the API for saving and retrieving the shopping cart state