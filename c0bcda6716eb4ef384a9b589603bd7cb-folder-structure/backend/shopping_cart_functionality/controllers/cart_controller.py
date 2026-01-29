# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.shopping_cart_functionality.services.cart_service import CartService
from backend.shopping_cart_functionality.repositories.cart_repository import CartRepository

cart_blueprint = Blueprint('cart_controller', __name__)
logger = get_logger(__name__)

@cart_blueprint.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = data.get('user_id')
    session_id = data.get('session_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    cart_repository = CartRepository()  # Ideally should be injected
    cart_service = CartService(cart_repository)
    
    success = cart_service.add_product_to_cart(user_id, session_id, product_id, quantity)
    if not success:
        return jsonify({'message': 'Failed to add product to cart'}), 400
    
    return jsonify({'message': 'Product added to cart successfully'})