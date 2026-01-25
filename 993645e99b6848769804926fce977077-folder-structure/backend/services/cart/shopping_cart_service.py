from backend.repositories.cart.shopping_cart_repository import ShoppingCartRepository
from backend.models.cart import Cart

class ShoppingCartService:
    
    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> None:
        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            cart = Cart(user_id=user_id, items={product_id: quantity})
        else:
            if product_id in cart.items:
                cart.items[product_id] += quantity
            else:
                cart.items[product_id] = quantity
        self.shopping_cart_repository.save_cart(cart)
    
    def remove_product_from_cart(self, user_id: int, product_id: int) -> None:
        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart or product_id not in cart.items:
            raise ValueError("Product not found in cart")
        
        del cart.items[product_id]
        self.shopping_cart_repository.save_cart(cart)
    
    def modify_product_quantity(self, user_id: int, product_id: int, quantity: int) -> None:
        cart = self.shopping_cart_repository.get_cart_by_user_id(user_id)
        if not cart or product_id not in cart.items:
            raise ValueError("Product not found in cart")
        
        cart.items[product_id] = quantity
        self.shopping_cart_repository.save_cart(cart)