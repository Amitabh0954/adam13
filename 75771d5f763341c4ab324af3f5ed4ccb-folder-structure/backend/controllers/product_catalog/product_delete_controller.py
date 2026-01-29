# Epic Title: Delete Product

from flask import Blueprint, request, jsonify
from services.product_catalog.product_delete_service import ProductDeleteService
from validators.product_catalog.product_delete_validator import ProductDeleteValidator

product_delete_controller = Blueprint('product_delete_controller', __name__)

@product_delete_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    data = request.get_json()
    validator = ProductDeleteValidator(data)
    if validator.is_valid():
        service = ProductDeleteService()
        response = service.delete_product(product_id)
        return jsonify(response), 200
    return jsonify(validator.errors), 400