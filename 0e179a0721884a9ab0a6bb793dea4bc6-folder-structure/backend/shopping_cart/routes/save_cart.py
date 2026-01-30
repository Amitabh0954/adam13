# Epic Title: Shopping Cart Functionality
from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from services.shopping_cart_service import ShoppingCartService

save_cart_bp = Blueprint('save_cart', __name__)
shopping_cart_service = ShoppingCartService()

@save_cart_bp.route('/cart/save', methods=['POST'])
@login_required
def save_cart():
    response = shopping_cart_service.save_cart(current_user.id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@save_cart_bp.route('/cart/retrieve', methods=['GET'])
@login_required
def retrieve_cart():
    response = shopping_cart_service.retrieve_cart(current_user.id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200