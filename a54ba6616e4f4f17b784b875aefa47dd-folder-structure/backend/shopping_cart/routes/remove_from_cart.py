# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from services.shopping_cart_service import ShoppingCartService
from flask_login import login_required, current_user

remove_from_cart_bp = Blueprint('remove_from_cart', __name__)
shopping_cart_service = ShoppingCartService()

@remove_from_cart_bp.route('/remove', methods=['POST'])
@login_required
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    
    user_id = current_user.get_id()
    
    response = shopping_cart_service.remove_from_cart(user_id, product_id)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200