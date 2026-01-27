# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    cart_service = CartService()
    cart_service.add_to_cart(session, product_id, quantity)

    return jsonify({'message': 'Product added to cart successfully'}), 200

@cart_bp.route('/', methods=['GET'])
def get_cart():
    cart_service = CartService()
    cart_contents = cart_service.get_cart(session)
    return jsonify(cart_contents), 200

@cart_bp.route('/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    cart_service = CartService()
    cart_service.remove_from_cart(session, product_id)

    return jsonify({'message': 'Product removed from cart successfully'}), 200