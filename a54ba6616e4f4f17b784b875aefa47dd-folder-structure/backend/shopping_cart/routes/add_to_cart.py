# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from services.shopping_cart_service import ShoppingCartService
from flask_login import login_required, current_user

add_to_cart_bp = Blueprint('add_to_cart', __name__)
shopping_cart_service = ShoppingCartService()

@add_to_cart_bp.route('/add', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    user_id = current_user.get_id()
    
    response = shopping_cart_service.add_to_cart(user_id, product_id, quantity)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200