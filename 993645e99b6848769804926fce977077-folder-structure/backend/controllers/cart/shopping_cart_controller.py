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