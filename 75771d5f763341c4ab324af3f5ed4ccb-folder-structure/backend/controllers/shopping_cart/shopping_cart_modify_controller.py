# Epic Title: Modify Quantity of Products in Shopping Cart

from flask import Blueprint, request, jsonify
from services.shopping_cart.shopping_cart_modify_service import ShoppingCartModifyService
from validators.shopping_cart.shopping_cart_modify_validator import ShoppingCartModifyValidator

shopping_cart_modify_controller = Blueprint('shopping_cart_modify_controller', __name__)

@shopping_cart_modify_controller.route('/cart', methods=['PUT'])
def modify_cart_quantity():
    data = request.get_json()
    validator = ShoppingCartModifyValidator(data)
    if validator.is_valid():
        service = ShoppingCartModifyService()
        response = service.modify_cart_quantity(data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400