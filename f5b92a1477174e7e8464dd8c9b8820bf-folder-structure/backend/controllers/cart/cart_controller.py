from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from backend.services.cart.cart_service import CartService
import logging

logger = logging.getLogger(__name__)
cart_bp = Blueprint('cart', __name__)

cart_service = CartService()

@cart_bp.route('/cart', methods=['GET'])
@login_required
def get_cart():
    cart = cart_service.get_cart(current_user.id)
    return jsonify(cart), 200

@cart_bp.route('/cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        logger.warning("Product ID is required")
        return jsonify({"message": "Product ID is required"}), 400

    cart = cart_service.add_to_cart(current_user.id, product_id, quantity)
    return jsonify(cart), 201