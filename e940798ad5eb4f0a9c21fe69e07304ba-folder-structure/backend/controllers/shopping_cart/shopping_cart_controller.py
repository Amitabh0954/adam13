# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from backend.services.shopping_cart.shopping_cart_service import ShoppingCartService

shopping_cart_bp = Blueprint('shopping_cart', __name__)
shopping_cart_service = ShoppingCartService()

@shopping_cart_bp.route('/api/shopping_cart/add', methods=['POST'])
def add_product_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not user_id or not product_id or not quantity:
        return jsonify({"error": "User ID, product ID, and quantity are required"}), 400

    response = shopping_cart_service.add_product_to_cart(user_id, product_id, quantity)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200

@shopping_cart_bp.route('/api/shopping_cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    cart_items = shopping_cart_service.get_cart(int(user_id))
    return jsonify(cart_items), 200

@shopping_cart_bp.route('/api/shopping_cart/clear', methods=['DELETE'])
def clear_cart():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    response = shopping_cart_service.clear_cart(int(user_id))
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200

@shopping_cart_bp.route('/api/shopping_cart/remove', methods=['DELETE'])
def remove_product_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    confirmation = data.get('confirmation')

    if not user_id or not product_id or not confirmation:
        return jsonify({"error": "User ID, product ID, and confirmation are required"}), 400

    response = shopping_cart_service.remove_product_from_cart(user_id, product_id, confirmation)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200