from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from backend.services.shopping_cart.shopping_cart_service import ShoppingCartService

shopping_cart_blueprint = Blueprint('shopping_cart', __name__)
shopping_cart_service = ShoppingCartService()

@shopping_cart_blueprint.route('/cart', methods=['GET'])
def get_cart():
    if current_user.is_authenticated:
        cart = shopping_cart_service.get_cart(current_user.id)
    else:
        cart = session.get('cart', {})
    return jsonify(cart), 200

@shopping_cart_blueprint.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    if current_user.is_authenticated:
        shopping_cart_service.add_to_cart(current_user.id, product_id, quantity)
        cart = shopping_cart_service.get_cart(current_user.id)
    else:
        cart = session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + quantity
        session['cart'] = cart
    return jsonify({"message": "Product added to cart", "cart": cart}), 200

@shopping_cart_blueprint.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    confirm = data.get('confirm', False)
    if not confirm:
        return jsonify({"error": "Confirmation required"}), 400

    if current_user.is_authenticated:
        shopping_cart_service.remove_from_cart(current_user.id, product_id)
        cart = shopping_cart_service.get_cart(current_user.id)
    else:
        cart = session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            session['cart'] = cart
    return jsonify({"message": "Product removed from cart", "cart": cart}), 200