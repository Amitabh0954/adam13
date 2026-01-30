# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from services.shopping_cart_service import ShoppingCartService
from flask_login import login_required, current_user

modify_cart_quantity_bp = Blueprint('modify_cart_quantity', __name__)
shopping_cart_service = ShoppingCartService()

@modify_cart_quantity_bp.route('/modify_quantity', methods=['POST'])
@login_required
def modify_quantity():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    if quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    user_id = current_user.get_id()
    
    response = shopping_cart_service.modify_quantity(user_id, product_id, quantity)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200