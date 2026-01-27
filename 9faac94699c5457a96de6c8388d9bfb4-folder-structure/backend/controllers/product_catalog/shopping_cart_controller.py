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

@shopping_cart_bp.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    confirmation = request.json.get('confirmation')
    if not confirmation or confirmation.lower() != 'yes':
        return jsonify({'message': 'Deletion not confirmed'}), 400

    user_service = UserService()
    if not user_service.is_user_logged_in():
        cart = session.get('cart', {})
    else:
        user_id = user_service.get_current_user_id()
        cart = user_service.get_user_cart(user_id)

    if product_id not in cart:
        return jsonify({'message': 'Product not in cart'}), 400

    shopping_cart_service = ShoppingCartService()
    result = shopping_cart_service.remove_product_from_cart(cart, product_id)

    if user_service.is_user_logged_in():
        user_service.save_user_cart(user_id, cart)
        message = 'Product removed from cart for logged-in user'
    else:
        session['cart'] = cart
        message = 'Product removed from cart for guest user'

    return jsonify({'message': message, 'total_price': result['total_price']}), 200

@shopping_cart_bp.route('/cart/<int:product_id>', methods=['PUT'])
def modify_cart_quantity(product_id):
    data = request.get_json()
    quantity = data.get('quantity')

    if not quantity or quantity <= 0:
        return jsonify({'message': 'Quantity must be a positive integer'}), 400

    user_service = UserService()
    if not user_service.is_user_logged_in():
        cart = session.get('cart', {})
    else:
        user_id = user_service.get_current_user_id()
        cart = user_service.get_user_cart(user_id)

    if product_id not in cart:
        return jsonify({'message': 'Product not in cart'}), 400

    shopping_cart_service = ShoppingCartService()
    result = shopping_cart_service.modify_product_quantity(cart, product_id, quantity)

    if user_service.is_user_logged_in():
        user_service.save_user_cart(user_id, cart)
        message = 'Product quantity modified for logged-in user'
    else:
        session['cart'] = cart
        message = 'Product quantity modified for guest user'

    return jsonify({'message': message, 'total_price': result['total_price']}), 200

@shopping_cart_bp.route('/cart', methods=['GET'])
def get_cart():
    user_service = UserService()
    if user_service.is_user_logged_in():
        user_id = user_service.get_current_user_id()
        cart = user_service.get_user_cart(user_id) or {}
        message = 'Cart retrieved for logged-in user'
    else:
        cart = session.get('cart', {})
        message = 'Cart retrieved for guest user'
    
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return jsonify({'message': message, 'cart': cart, 'total_price': total_price}), 200