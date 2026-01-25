from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.cart.cart_service import CartService
import logging

logger = logging.getLogger(__name__)
cart_bp = Blueprint('cart', __name__)

cart_service = CartService()

@cart_bp.route('/cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    if not product_id:
        logger.warning("Product ID is required")
        return jsonify({"message": "Product ID is required"}), 400

    try:
        cart_service.add_to_cart(current_user.id, product_id, quantity)
        logger.info(f"Product with ID '{product_id}' added to cart for user '{current_user.id}'")
        return jsonify({"message": "Product added to cart successfully"}), 201
    except ValueError as e:
        logger.warning(f"Failed to add product to cart: {str(e)}")
        return jsonify({"message": str(e)}), 400

@cart_bp.route('/cart')
@login_required
def get_cart():
    try:
        cart_items = cart_service.get_cart(current_user.id)
        logger.info(f"Cart retrieved for user '{current_user.id}'")
        return jsonify({"cart_items": [item.to_dict() for item in cart_items]}), 200
    except ValueError as e:
        logger.warning(f"Failed to retrieve cart: {str(e)}")
        return jsonify({"message": str(e)}), 400

@cart_bp.route('/cart/<int:cart_item_id>', methods=['DELETE'])
@login_required
def remove_from_cart(cart_item_id: int):
    if not request.json.get('confirmation', False):
        logger.warning("Confirmation is required to remove item from cart")
        return jsonify({"message": "Confirmation is required"}), 400

    try:
        cart_service.remove_from_cart(current_user.id, cart_item_id)
        logger.info(f"Cart item with ID '{cart_item_id}' removed for user '{current_user.id}'")
        return jsonify({"message": "Cart item removed successfully"}), 200
    except ValueError as e:
        logger.warning(f"Failed to remove cart item: {str(e)}")
        return jsonify({"message": str(e)}), 400