# Epic Title: Add Product to Shopping Cart

from flask import Blueprint, request, jsonify
from services.shopping_cart.shopping_cart_service import ShoppingCartService
from validators.shopping_cart.shopping_cart_validator import ShoppingCartValidator

shopping_cart_controller = Blueprint('shopping_cart_controller', __name__)

@shopping_cart_controller.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    validator = ShoppingCartValidator(data)
    if validator.is_valid():
        service = ShoppingCartService()
        response = service.add_to_cart(data)
        return jsonify(response), 201
    return jsonify(validator.errors), 400