# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from backend.services.cart_service import CartService

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        return jsonify({'message': 'Product ID is required'}), 400

    user_id = session.get('user_id')
    cart_service = CartService()
    result = cart_service.add_to_cart(user_id, product_id, quantity)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product added to cart successfully'}), 201

@cart_bp.route('/delete', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({'message': 'Product ID is required'}), 400

    user_id = session.get('user_id')
    cart_service = CartService()
    result = cart_service.remove_from_cart(user_id, product_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product removed from cart successfully'}), 200

@cart_bp.route('/update_quantity', methods=['POST'])
def update_quantity():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or quantity is None:
        return jsonify({'message': 'Product ID and quantity are required'}), 400

    if quantity <= 0:
        return jsonify({'message': 'Quantity must be a positive integer'}), 400

    user_id = session.get('user_id')
    cart_service = CartService()
    result = cart_service.update_quantity(user_id, product_id, quantity)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product quantity updated successfully'}), 200

@cart_bp.route('/save', methods=['POST'])
def save_cart():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'message': 'User must be logged in to save the cart'}), 400

    cart_service = CartService()
    result = cart_service.save_cart(user_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Cart saved successfully'}), 200

@cart_bp.route('/load', methods=['GET'])
def load_cart():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'message': 'User must be logged in to load the cart'}), 400

    cart_service = CartService()
    result = cart_service.load_cart(user_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify(result), 200