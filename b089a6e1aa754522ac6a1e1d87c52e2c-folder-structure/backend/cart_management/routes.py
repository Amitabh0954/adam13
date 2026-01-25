import logging
from flask import Blueprint, request, jsonify, session
from .models import db, Cart, CartItem
from backend.product_management.catalog.models import Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)

    if not product_id or quantity <= 0:
        return jsonify({'message': 'Invalid product ID or quantity'}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    cart = None
    if 'user_id' in session:
        user_id = session['user_id']
        cart = Cart.query.filter_by(user_id=user_id).first()
    elif 'session_id' in session:
        session_id = session['session_id']
        cart = Cart.query.filter_by(session_id=session_id).first()

    if not cart:
        cart = Cart(user_id=session.get('user_id'), session_id=session.get('session_id'))
        db.session.add(cart)
        db.session.commit()

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()

    logger.info(f"Product {product_id} added to cart")
    return jsonify({'message': 'Product added to cart successfully'}), 201

@cart_bp.route('/cart/item/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id: int):
    confirm = request.args.get('confirm', 'false').lower() == 'true'
    if not confirm:
        return jsonify({'message': 'Confirmation required to remove item'}), 400

    cart_item = CartItem.query.get(item_id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404

    product_name = cart_item.product.name
    db.session.delete(cart_item)
    db.session.commit()

    logger.info(f"Product {product_name} removed from cart")
    return jsonify({'message': 'Product removed from cart successfully'}), 200

@cart_bp.route('/cart/total', methods=['GET'])
def get_cart_total():
    cart = None
    if 'user_id' in session:
        user_id = session['user_id']
        cart = Cart.query.filter_by(user_id=user_id).first()
    elif 'session_id' in session:
        session_id = session['session_id']
        cart = Cart.query.filter_by(session_id=session_id).first()

    if not cart:
        return jsonify({'total_price': 0.0}), 200

    total_price = sum(item.quantity * item.product.price for item in cart.items)

    return jsonify({'total_price': total_price}), 200