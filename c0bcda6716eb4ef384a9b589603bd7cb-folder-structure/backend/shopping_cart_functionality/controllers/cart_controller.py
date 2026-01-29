# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.shopping_cart_functionality.services.cart_service import CartService
from backend.shopping_cart_functionality.repositories.cart_repository import CartRepository

cart_blueprint = Blueprint('cart_controller', __name__)
logger = get_logger(__name__)

@cart_blueprint.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = data.get('user_id')
    session_id = data.get('session_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    cart_repository = CartRepository()  # Ideally should be injected
    cart_service = CartService(cart_repository)
    
    success = cart_service.add_product_to_cart(user_id, session_id, product_id, quantity)
    if not success:
        return jsonify({'message': 'Failed to add product to cart'}), 400
    
    return jsonify({'message': 'Product added to cart successfully'})

@cart_blueprint.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.json
    user_id = data.get('user_id')
    session_id = data.get('session_id')
    product_id = data.get('product_id')

    cart_repository = CartRepository()  # Ideally should be injected
    cart_service = CartService(cart_repository)

    success = cart_service.remove_product_from_cart(user_id, session_id, product_id)
    if not success:
        return jsonify({'message': 'Failed to remove product from cart'}), 400
    
    return jsonify({'message': 'Product removed from cart successfully'})

@cart_blueprint.route('/cart/modify', methods=['POST'])
def modify_quantity_in_cart():
    data = request.json
    user_id = data.get('user_id')
    session_id = data.get('session_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not isinstance(quantity, int) or quantity <= 0:
        return jsonify({'message': 'Quantity must be a positive integer'}), 400

    cart_repository = CartRepository()  # Ideally should be injected
    cart_service = CartService(cart_repository)

    success = cart_service.modify_quantity_in_cart(user_id, session_id, product_id, quantity)
    if not success:
        return jsonify({'message': 'Failed to modify quantity in cart'}), 400
    
    return jsonify({'message': 'Quantity modified successfully'})

@cart_blueprint.route('/cart/save', methods=['POST'])
def save_cart_state():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    cart_repository = CartRepository()  # Ideally should be injected
    cart_service = CartService(cart_repository)
    
    success = cart_service.save_cart_state(user_id)
    if not success:
        return jsonify({'message': 'Failed to save cart state'}), 400

    return jsonify({'message': 'Cart state saved successfully'})

@cart_blueprint.route('/cart/load', methods=['POST'])
def load_cart_state():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    cart_repository = CartRepository()  # Ideally should be injected
    cart_service = CartService(cart_repository)
    
    cart_state = cart_service.load_cart_state(user_id)
    if cart_state is None:
        return jsonify({'message': 'Failed to load cart state'}), 400

    return jsonify({'cart_state': cart_state})