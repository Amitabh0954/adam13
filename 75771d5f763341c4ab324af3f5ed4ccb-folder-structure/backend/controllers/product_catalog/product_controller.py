# Epic Title: Add New Product

from flask import Blueprint, request, jsonify
from services.product_catalog.product_service import ProductService
from validators.product_catalog.product_validator import ProductValidator

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    validator = ProductValidator(data)
    if validator.is_valid():
        service = ProductService()
        response = service.add_product(data)
        return jsonify(response), 201
    return jsonify(validator.errors), 400