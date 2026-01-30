# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify, session
from services.shopping_cart_service import ShoppingCartService

remove_from_cart_bp = Blueprint('remove_from_cart', __name__)
cart_service = ShoppingCartService()

@remove_from_cart_bp.route('/remove', methods=['DELETE'])
def remove_from_cart():
    if 'user_id' not in session:
        return jsonify({"error": "User must be logged in to remove products from cart"}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    product_id = data.get('product_id')
    
    response = cart_service.remove_product_from_cart(user_id, product_id)
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200