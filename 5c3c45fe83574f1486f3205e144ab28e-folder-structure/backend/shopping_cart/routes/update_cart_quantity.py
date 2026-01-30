# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify, session
from services.shopping_cart_service import ShoppingCartService

update_cart_quantity_bp = Blueprint('update_cart_quantity', __name__)
cart_service = ShoppingCartService()

@update_cart_quantity_bp.route('/update_quantity', methods=['PUT'])
def update_cart_quantity():
    if 'user_id' not in session:
        return jsonify({"error": "User must be logged in to update product quantity in cart"}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    if quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400
    
    response = cart_service.update_product_quantity(user_id, product_id, quantity)
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200