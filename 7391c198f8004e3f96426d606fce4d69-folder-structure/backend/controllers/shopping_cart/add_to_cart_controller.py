from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from backend.repositories.shopping_cart.cart_repository import CartRepository
from backend.repositories.product_catalog.product_repository import ProductRepository

add_to_cart_controller = Blueprint('add_to_cart_controller', __name__)
cart_repository = CartRepository()
product_repository = ProductRepository()

@add_to_cart_controller.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    product = product_repository.get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found