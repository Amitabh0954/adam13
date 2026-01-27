from backend.repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository
from backend.models.shopping_cart import ShoppingCartItem

class ShoppingCartService:
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def get_cart(self, user_id: int) -> dict:
        cart_items = self.shopping_cart_repository.find_by_user_id(user_id)
        return {"items": { item.product_id: item.quantity for item in cart_items }, "total": self.calculate_total(cart_items)}

    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        cart_item = self.shopping_cart_repository.find_by_user_id_and_product_id(user_id, product_id)
        if cart_item:
            cart_item.quantity += quantity
            self.shopping_cart_repository.update_item(cart_item)
        else:
            new_item = ShoppingCartItem(user_id=user_id, product_id=product_id, quantity=quantity)
            self.shopping_cart_repository.save_item(new_item)

    def remove_from_cart(self, user_id: int, product_id: int):
        cart_item = self.shopping_cart_repository.find_by_user_id_and_product_id(user_id, product_id)
        if cart_item:
            self.shopping_cart_repository.delete_item(cart_item)
    
    def calculate_total(self, cart_items: list[ShoppingCartItem]) -> float:
        return sum(item.product.price * item.quantity for item in cart_items)