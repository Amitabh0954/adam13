from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from backend.services.cart.shopping_cart_service import ShoppingCartService
import logging

logger = logging.getLogger(__name__)
cart_bp = Blueprint('cart', __name__)

shopping_cart_service = ShoppingCartService()

@cart_bp.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        logger.warning("Product ID is required")
        return jsonify({"message": "Product ID is required"}), 400

    if current_user.is_authenticated:
        user_id = current_user.id
        shopping_cart_service.add_product_to_cart(user_id, product_id, quantity)
        logger.info(f"Product {product_id} added to user {user_id}'s cart")
    else:
        cart = session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        session['cart'] = cart
        logger.info(f"Product {product_id} added to guest's cart")

    return jsonify({"message": "Product added to cart"}), 200

@cart_bp.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    confirmation = data.get('confirmation')

    if not product_id:
        logger.warning("Product ID is required")
        return jsonify({"message": "Product ID is required"}), 400

    if confirmation != "CONFIRM":
        logger.warning("Removal not confirmed")
        return jsonify({"message": "Confirmation is required"}), 400

    if current_user.is_authenticated:
        user_id = current_user.id
        shopping_cart_service.remove_product_from_cart(user_id, product_id)
        logger.info(f"Product {product_id} removed from user {user_id}'s cart")
    else:
        cart = session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            session['cart'] = cart
            logger.info(f"Product {product_id} removed from guest's cart")
        else:
            logger.warning(f"Product {product_id} not found in guest's cart")
            return jsonify({"message": "Product not found in cart"}), 404

    return jsonify({"message": "Product removed from cart"}), 200

@cart_bp.route('/modify-cart', methods=['POST'])
def modify_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or quantity is None:
        logger.warning("Product ID and quantity are required")
        return jsonify({"message": "Product ID and quantity are required"}), 400

    if quantity <= 0:
        logger.warning("Quantity must be a positive integer")
        return jsonify({"message": "Quantity must be a positive integer"}), 400

    if current_user.is_authenticated:
        user_id = current_user.id
        shopping_cart_service.modify_product_quantity(user_id, product_id, quantity)
        logger.info(f"Product {product_id} quantity modified to {quantity} for user {user_id}")
    else:
        cart = session.get('cart', {})
        if product_id in cart:
            cart[product_id] = quantity
            session['cart'] = cart
            logger.info(f"Product {product_id} quantity modified to {quantity} in guest's cart")
        else:
            logger.warning(f"Product {product_id} not found in guest's cart")
            return jsonify({"message": "Product not found in cart"}), 404

    return jsonify({"message": "Product quantity modified"}), 200