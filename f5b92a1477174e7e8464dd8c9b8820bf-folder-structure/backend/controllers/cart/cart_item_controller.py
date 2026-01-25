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