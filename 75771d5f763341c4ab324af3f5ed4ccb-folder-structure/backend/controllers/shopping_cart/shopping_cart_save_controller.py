# Epic Title: Save Shopping Cart for Logged-in Users

from flask import Blueprint, request, jsonify
from services.shopping_cart.shopping_cart_save_service import ShoppingCartSaveService
from validators.shopping_cart.shopping_cart_save_validator import ShoppingCartSaveValidator

shopping_cart_save_controller = Blueprint('shopping_cart_save_controller', __name__)

@shopping_cart_save_controller.route('/cart/save', methods=['POST'])
def save_cart():
    data = request.get_json()
    validator = ShoppingCartSaveValidator(data)
    if validator.is_valid():
        service = ShoppingCartSaveService()
        response = service.save_cart(data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400

@shopping_cart_save_controller.route('/cart/load/<int:user_id>', methods=['GET'])
def load_cart(user_id: int):
    service = ShoppingCartSaveService()
    response = service.load_cart(user_id)
    return jsonify(response), 200