# Epic Title: Shopping Cart Functionality

from flask import Blueprint, request, jsonify, session
from models import Product, Cart, CartItem, User
from database import db_session

add_bp = Blueprint('add_bp', __name__)

@add_bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    user_id = session.get('user_id')  # Assume user_id is stored in the session on login
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    if user_id:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            cart = Cart(user_id=user_id)
            db_session.add(cart)
    else:
        cart_id = session.get('cart_id')
        cart = Cart.query.get(cart_id)
        if not cart:
            cart = Cart()
            db_session.add(cart)
            db_session.commit()
            session['cart_id'] = cart.id

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product.id, quantity=quantity)
        db_session.add(cart_item)

    db_session.commit()

    return jsonify({'message': 'Product added to cart'}), 200