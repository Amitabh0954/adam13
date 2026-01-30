# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from services.shopping_cart_service import ShoppingCartService

modify_cart_quantity_bp = Blueprint('modify_cart_quantity', __name__)
shopping_cart_service = ShoppingCartService()

@modify_cart_quantity_bp.route('/modify-cart-quantity', methods=['PUT'])
@login_required
def modify_cart_quantity():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or quantity is None:
        return jsonify({"error": "Product ID and quantity are required"}), 400

    if quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    response = shopping_cart_service.modify_cart_quantity(current_user.id, product_id, quantity)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200