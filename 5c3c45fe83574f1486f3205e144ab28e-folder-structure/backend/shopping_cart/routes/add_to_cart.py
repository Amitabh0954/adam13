# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify, session
from services.shopping_cart_service import ShoppingCartService

add_to_cart_bp = Blueprint('add_to_cart', __name__)
cart_service = ShoppingCartService()

@add_to_cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return jsonify({"error": "User must be logged in to add products to cart"}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    response = cart_service.add_product_to_cart(user_id, product_id, quantity)
    if response.get("error"):
        return jsonify(response), 400
    return jsonify(response), 201