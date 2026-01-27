# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from models import Cart, CartItem
from database import db_session

remove_bp = Blueprint('remove_bp', __name__)

@remove_bp.route('/cart/remove', methods=['DELETE'])
def remove_from_cart():
    user_id = session.get('user_id')  # Assume user_id is stored in the session on login
    data = request.get_json()
    product_id = data.get('product_id')

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

    db_session.delete(cart_item)
    db_session.commit()

    # Optionally implement a method to calculate the new total price if required
    total_price = sum(item.product.price * item.quantity for item in cart.items)
    
    return jsonify({'message': 'Product removed from cart', 'total_price': total_price}), 200