# Epic Title: Shopping Cart Functionality
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.shopping_cart_service import ShoppingCartService

add_product_to_cart_bp = Blueprint('add_product_to_cart', __name__)
shopping_cart_service = ShoppingCartService()

@add_product_to_cart_bp.route('/cart', methods=['POST'])
@login_required
def add_product_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id or quantity <= 0:
        return jsonify({"error": "Valid product ID and quantity are required"}), 400

    response = shopping_cart_service.add_product_to_cart(current_user.id, product_id, quantity)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 201