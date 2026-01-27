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