# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.shopping_cart_service import ShoppingCartService

modify_quantity_bp = Blueprint('modify_quantity', __name__)
shopping_cart_service = ShoppingCartService()

@modify_quantity_bp.route('/cart/<int:cart_item_id>', methods=['PUT'])
@login_required
def modify_quantity(cart_item_id):
    data = request.get_json()
    quantity = data.get('quantity')

    if not quantity or quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    response = shopping_cart_service.modify_quantity(current_user.id, cart_item_id, quantity)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200