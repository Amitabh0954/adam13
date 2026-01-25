import logging
from flask import Blueprint, request, jsonify, session
from .models import db, User
from backend.cart_management.models import Cart, CartItem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    session['user_id'] = user.id
    session['role'] = user.role

    logger.info(f"User {username} logged in successfully")
    return jsonify({'message': 'Logged in successfully'}), 200

@user_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    logger.info("User logged out successfully")
    return jsonify({'message': 'Logged out successfully'}), 200

@user_bp.route('/cart/transfer', methods=['POST'])
def transfer_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not logged in'}), 401

    session_cart = Cart.query.filter_by(session_id=session.get('session_id')).first()
    if not session_cart:
        return jsonify({'message': 'No cart to transfer'}), 200

    user_cart = Cart.query.filter_by(user_id=user_id).first()
    if not user_cart:
        user_cart = Cart(user_id=user_id)
        db.session.add(user_cart)
        db.session.commit()

    for item in session_cart.items:
        existing_item = CartItem.query.filter_by(cart_id=user_cart.id, product_id=item.product_id).first()
        if existing_item:
            existing_item.quantity += item.quantity
        else:
            new_item = CartItem(cart_id=user_cart.id, product_id=item.product_id, quantity=item.quantity)
            db.session.add(new_item)

    db.session.delete(session_cart)
    db.session.commit()

    logger.info(f"Cart transferred to user {user_id}")
    return jsonify({'message': 'Cart transferred successfully'}), 200