# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify, session
from services.shopping_cart_service import ShoppingCartService

save_cart_bp = Blueprint('save_cart', __name__)
cart_service = ShoppingCartService()

@save_cart_bp.route('/save', methods=['POST'])
def save_cart():
    if 'user_id' not in session:
        return jsonify({"error": "User must be logged in to save shopping cart"}), 401

    user_id = session['user_id']
    response = cart_service.save_cart(user_id)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200