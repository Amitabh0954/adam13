# Epic Title: Update Product Details

from flask import Blueprint, request, jsonify
from services.product_catalog.product_update_service import ProductUpdateService
from validators.product_catalog.product_update_validator import ProductUpdateValidator

product_update_controller = Blueprint('product_update_controller', __name__)

@product_update_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    validator = ProductUpdateValidator(data)
    if validator.is_valid():
        service = ProductUpdateService()
        response = service.update_product(product_id, data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400