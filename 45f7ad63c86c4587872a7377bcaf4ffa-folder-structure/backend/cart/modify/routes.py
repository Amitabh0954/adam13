# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from models import Cart, CartItem
from database import db_session

modify_bp = Blueprint('modify_bp', __name__)

@modify_bp.route('/cart/modify', methods=['PUT'])
def modify_cart():
    user_id = session.get('user_id')  # Assume user_id is stored in the session on login
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if quantity is None or quantity <= 0:
        return jsonify({'message': 'Quantity must be a positive integer'}), 400

    if user_id:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            return jsonify({'message': 'Cart not found'}), 404
    else:
        cart_id = session.get('cart_id')
        cart = Cart.query.get(cart_id)
        if not cart:
            return jsonify({'message': 'Cart not found'}), 404

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if not cart_item:
        return jsonify({'message': 'Product not in cart'}), 404

    cart_item.quantity = quantity
    db_session.commit()

    # Optionally implement a method to calculate the new total price if required
    total_price = sum(item.product.price * item.quantity for item in cart.items)

    return jsonify({'message': 'Cart updated successfully', 'total_price': total_price}), 200