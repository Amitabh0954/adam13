from flask import Blueprint, request, jsonify, session
from backend.services.catalog_management.cart_service import CartService
from flask_login import current_user

cart_blueprint = Blueprint('cart', __name__)
cart_service = CartService()

# Inline comment referencing the Epic Title
# Epic Title: Shopping Cart Functionality

@cart_blueprint.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    try:
        if current_user.is_authenticated:
            cart_service.add_to_cart(user_id=current_user.id, product_id=product_id, quantity=quantity)
        else:
            cart = session.get('cart', {})
            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity
            session['cart'] = cart

        return jsonify({"message": "Product added to cart successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@cart_blueprint.route('/cart', methods=['GET'])
def get_cart():
    try:
        if current_user.is_authenticated:
            cart = cart_service.get_user_cart(user_id=current_user.id)
        else:
            cart = session.get('cart', {})
            cart = cart_service.get_guest_cart(cart)

        return jsonify(cart), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@cart_blueprint.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    try:
        if current_user.is_authenticated:
            cart_service.remove_from_cart(user_id=current_user.id, product_id=product_id)
        else:
            cart = session.get('cart', {})
            if product_id in cart:
                del cart[product_id]
                session['cart'] = cart

        return jsonify({"message": "Product removed from cart successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400