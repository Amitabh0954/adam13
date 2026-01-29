# Epic Title: Remove Product from Shopping Cart

from flask import Blueprint, request, jsonify
from services.shopping_cart.shopping_cart_remove_service import ShoppingCartRemoveService
from validators.shopping_cart.shopping_cart_remove_validator import ShoppingCartRemoveValidator

shopping_cart_remove_controller = Blueprint('shopping_cart_remove_controller', __name__)

@shopping_cart_remove_controller.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    validator = ShoppingCartRemoveValidator(data)
    if validator.is_valid():
        service = ShoppingCartRemoveService()
        response = service.remove_from_cart(data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400