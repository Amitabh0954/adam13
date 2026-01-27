# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if quantity <= 0:
        return jsonify({'message': 'Quantity must be a positive integer'}), 400

    cart_service = CartService()
    cart_service.add_to_cart(session, product_id, quantity)

    cart_contents = cart_service.get_cart(session)
    session['cart'] = cart_contents
    return jsonify({'message': 'Product added to cart successfully', 'cart': cart_contents}), 200

@cart_bp.route('/', methods=['GET'])
def get_cart():
    cart_service = CartService()
    cart_contents = cart_service.get_cart(session)
    return jsonify(cart_contents), 200

@cart_bp.route('/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    confirmation = data.get('confirmation')
    if not confirmation:
        return jsonify({'message': 'Remove confirmation required'}), 400

    cart_service = CartService()
    cart_service.remove_from_cart(session, product_id)

    cart_contents = cart_service.get_cart(session)
    session['cart'] = cart_contents
    return jsonify({'message': 'Product removed from cart successfully', 'cart': cart_contents}), 200

@cart_bp.route('/update_quantity', methods=['POST'])
def update_quantity():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if quantity <= 0:
        return jsonify({'message': 'Quantity must be a positive integer'}), 400

    cart_service = CartService()
    cart_service.update_quantity(session, product_id, quantity)

    cart_contents = cart_service.get_cart(session)
    session['cart'] = cart_contents
    return jsonify({'message': 'Product quantity updated successfully', 'cart': cart_contents}), 200

@cart_bp.route('/save', methods=['POST'])
def save_cart():
    if not session.get('user_id'):
        return jsonify({'message': 'User must be logged in to save cart'}), 403

    cart_service = CartService()
    cart_service.save_cart(session)
    return jsonify({'message': 'Cart saved successfully'}), 200

@cart_bp.route('/load', methods=['GET'])
def load_cart():
    if not session.get('user_id'):
        return jsonify({'message': 'User must be logged in to load cart'}), 403

    cart_service = CartService()
    cart_contents = cart_service.load_cart(session)
    session['cart'] = cart_contents
    return jsonify(cart_contents), 200