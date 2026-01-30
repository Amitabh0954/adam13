# Epic Title: Save Shopping Cart for Logged-in Users

from backend.cart.models.cart import Cart, CartItem
from backend.products.models.product import Product
from backend.accounts.models.user import User
from typing import Optional

class CartRepository:
    def create_cart(self, user: Optional[User] = None, session_id: Optional[str] = None) -> Cart:
        cart = Cart(user=user, session_id=session_id)
        cart.save()
        return cart

    def get_cart(self, user: Optional[User] = None, session_id: Optional[str] = None) -> Optional[Cart]:
        if user:
            return Cart.objects.filter(user=user).first()
        elif session_id:
            return Cart.objects.filter(session_id=session_id).first()
        return None

    def add_product(self, cart: Cart, product: Product, quantity: int) -> CartItem:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()
        
        # Update the total price of the cart
        cart.total_price += product.price * quantity
        cart.save()

        return cart_item

    def remove_product(self, cart: Cart, product: Product) -> None:
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            # Update the total price of the cart
            cart.total_price -= product.price * cart_item.quantity
            cart.total_price = max(cart.total_price, 0)
            cart.save()
            
            cart_item.delete()

    def modify_product_quantity(self, cart: Cart, product: Product, new_quantity: int) -> CartItem:
        if new_quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if not cart_item:
            raise ValueError("Product not found in cart")

        # Update the total price of the cart
        cart.total_price -= product.price * cart_item.quantity
        cart_item.quantity = new_quantity
        cart_item.save()
        cart.total_price += product.price * new_quantity
        cart.save()
        
        return cart_item

    def clear_cart(self, cart: Cart) -> None:
        CartItem.objects.filter(cart=cart).delete()
        cart.total_price = 0
        cart.save()