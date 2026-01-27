# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from backend.services.product_catalog.shopping_cart_service import ShoppingCartService
from backend.services.product_catalog.user_service import UserService

shopping_cart_bp = Blueprint('shopping_cart_bp', __name__)

@shopping_cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        return jsonify({'message': 'Product ID is required'}), 400

    user_service = UserService()
    if not user_service.is_user_logged_in():
        cart = session.get('cart', {})
    else:
        user_id = user_service.get_current_user_id()
        cart = user_service.get_user_cart(user_id)

    shopping_cart_service = ShoppingCartService()
    result = shopping_cart_service.add_product_to_cart(cart, product_id, quantity)

    if user_service.is_user_logged_in():
        user_service.save_user_cart(user_id, cart)
        message = 'Product added to cart for logged-in user'
    else:
        session['cart'] = cart
        message = 'Product added to cart for guest user'

    return jsonify({'message': message}), 200