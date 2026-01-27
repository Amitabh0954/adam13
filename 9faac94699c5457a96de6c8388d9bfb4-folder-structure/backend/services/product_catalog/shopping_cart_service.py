# Epic Title: Shopping Cart Functionality

from backend.repositories.product_catalog.product_repository import ProductRepository
from typing import Dict

class ShoppingCartService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product_to_cart(self, cart: Dict, product_id: int, quantity: int) -> dict:
        product = self.product_repository.get_product_by_id(product_id)
        if not product:
            return {'status': 'error', 'message': 'Product not found'}

        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {'name': product.name, 'price': product.price, 'quantity': quantity}

        return {'status': 'success', 'message': 'Product added to cart'}

    def remove_product_from_cart(self, cart: Dict, product_id: int) -> dict:
        if product_id in cart:
            del cart[product_id]
            total_price = sum(item['price'] * item['quantity'] for item in cart.values())
            return {'status': 'success', 'total_price': total_price}
        return {'status': 'error', 'message': 'Product not found in cart'}