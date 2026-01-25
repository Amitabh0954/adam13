from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.cart.cart_service import CartService
import logging

logger = logging.getLogger(__name__)
cart_item_bp = Blueprint('cart_item', __name__)

cart_service = CartService()

@cart_item_bp.route('/cart/items/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    try:
        cart_service.remove_from_cart(current_user.id, product_id)
        logger.info(f"Product with ID '{product_id}' removed from cart")
        return jsonify({"message": "Product removed from cart"}), 200
    except ValueError as e:
        logger.warning(f"Failed to remove product: {str(e)}")
        return jsonify({"message": str(e)}), 400

@cart_item_bp.route('/cart/items', methods=['PATCH'])
@login_required
def modify_cart_item():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or quantity is None:
        logger.warning("Product ID and quantity are required")
        return jsonify({"message": "Product ID and quantity are required"}), 400

    if quantity <= 0:
        logger.warning("Quantity must be a positive integer")
        return jsonify({"message": "Quantity must be a positive integer"}), 400

    try:
        cart_service.modify_cart_item(current_user.id, product_id, quantity)
        logger.info(f"Product with ID '{product_id}' quantity updated to {quantity}")
        return jsonify({"message": "Cart item quantity updated"}), 200
    except ValueError as e:
        logger.warning(f"Failed to update cart item quantity: {str(e)}")
        return jsonify({"message": str(e)}), 400