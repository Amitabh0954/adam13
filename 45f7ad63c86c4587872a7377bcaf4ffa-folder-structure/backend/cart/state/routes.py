# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from models import Cart, CartItem, User
from database import db_session

state_bp = Blueprint('state_bp', __name__)

@state_bp.route('/cart/save', methods=['POST'])
def save_cart_state():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not logged in'}), 401

    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    user = User.query.get(user_id)
    user.saved_cart = cart.to_json()  # Assuming Cart has a method to_json to serialize its state
    db_session.commit()
    
    return jsonify({'message': 'Cart state saved successfully'}), 200

@state_bp.route('/cart/load', methods=['GET'])
def load_cart_state():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not logged in'}), 401

    user = User.query.get(user_id)
    if not user.saved_cart:
        return jsonify({'message': 'No saved cart found'}), 404

    cart_data = user.load_cart()
    cart = Cart(user_id=user_id)
    db_session.add(cart)
    db_session.commit()
    for item_data in cart_data['items']:
        cart_item = CartItem(cart_id=cart.id, product_id=item_data['product_id'], quantity=item_data['quantity'])
        db_session.add(cart_item)
    db_session.commit()

    return jsonify(cart.to_json()), 200