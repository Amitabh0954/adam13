# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from services.shopping_cart_service import ShoppingCartService
from flask_login import login_required, current_user

save_cart_bp = Blueprint('save_cart', __name__)
shopping_cart_service = ShoppingCartService()

@save_cart_bp.route('/save', methods=['POST'])
@login_required
def save_cart():
    user_id = current_user.get_id()
    
    response = shopping_cart_service.save_cart(user_id)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200

@save_cart_bp.route('/retrieve', methods=['GET'])
@login_required
def retrieve_cart():
    user_id = current_user.get_id()
    
    response = shopping_cart_service.retrieve_cart(user_id)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200