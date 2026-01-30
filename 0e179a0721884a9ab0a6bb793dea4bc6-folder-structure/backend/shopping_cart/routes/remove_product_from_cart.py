# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.shopping_cart_service import ShoppingCartService

remove_product_from_cart_bp = Blueprint('remove_product_from_cart', __name__)
shopping_cart_service = ShoppingCartService()

@remove_product_from_cart_bp.route('/cart/<int:cart_item_id>', methods=['DELETE'])
@login_required
def remove_product_from_cart(cart_item_id):
    confirmation = request.args.get('confirmation')

    if confirmation != 'true':
        return jsonify({"error": "Confirmation is required to remove a product from the cart"}), 400

    response = shopping_cart_service.remove_product_from_cart(current_user.id, cart_item_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200