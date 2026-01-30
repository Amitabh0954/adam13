# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from services.shopping_cart_service import ShoppingCartService

remove_from_cart_bp = Blueprint('remove_from_cart', __name__)
shopping_cart_service = ShoppingCartService()

@remove_from_cart_bp.route('/remove-from-cart', methods=['DELETE'])
@login_required
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    confirmation = data.get('confirmation')

    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400

    if confirmation != 'CONFIRM':
        return jsonify({"error": "Remove confirmation required"}), 400

    response = shopping_cart_service.remove_from_cart(current_user.id, product_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200