# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from backend.shopping_cart_functionality.services.cart_service import CartService

cart_bp = Blueprint('cart_bp', __name__)
cart_service = CartService()

@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        return jsonify({'message': 'Product ID is required'}), 400

    user_id = session.get('user_id')  # For logged-in users
    
    result = cart_service.add_to_cart(user_id, product_id, quantity)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product added to cart'}), 200