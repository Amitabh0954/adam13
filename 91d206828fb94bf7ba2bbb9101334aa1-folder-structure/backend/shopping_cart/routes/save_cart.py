# Epic Title: Shopping Cart Functionality
from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from services.shopping_cart_service import ShoppingCartService

save_cart_bp = Blueprint('save_cart', __name__)
shopping_cart_service = ShoppingCartService()

@save_cart_bp.route('/save-cart', methods=['POST'])
@login_required
def save_cart():
    response = shopping_cart_service.save_cart(current_user.id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200