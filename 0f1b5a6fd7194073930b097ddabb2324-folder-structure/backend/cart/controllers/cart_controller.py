from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from backend.cart.repositories.cart_repository import CartRepository

cart_blueprint = Blueprint('cart', __name__)
cart_repository = CartRepository()

@cart_blueprint.route('/cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)

    if current_user.is_authenticated:
        cart = cart_repository.get_or_create_cart(user_id=current_user.id)
    else:
        if 'session_id' not in session:
            session['session_id'] = session.sid
        cart = cart_repository.get_or_create_cart(session_id=session['session_id'])

    cart_item = cart_repository.add_product_to_cart(cart.id, product_id, quantity)
    return jsonify({"message": "Product added to cart successfully", "cart_item": cart_item.to_dict()}), 201

@cart_blueprint.route('/cart', methods=['GET'])
def get_cart():
    if current_user.is_authenticated:
        cart = cart_repository.get_cart_by_user_id(current_user.id)
    else:
        if 'session_id' in session:
            cart = cart_repository.get_cart_by_session_id(session['session_id'])
        else:
            return jsonify({"cart": []}), 200

    if not cart:
        return jsonify({"cart": []}), 200
    
    cart_items = [item.to_dict() for item in cart.items]
    return jsonify({"cart": cart_items}), 200