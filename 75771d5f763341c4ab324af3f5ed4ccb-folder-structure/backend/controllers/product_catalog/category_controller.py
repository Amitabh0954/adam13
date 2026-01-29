# Epic Title: Product Categorization

from flask import Blueprint, request, jsonify
from services.product_catalog.category_service import CategoryService
from validators.product_catalog.category_validator import CategoryValidator

category_controller = Blueprint('category_controller', __name__)

@category_controller.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    validator = CategoryValidator(data)
    if validator.is_valid():
        service = CategoryService()
        response = service.add_category(data)
        return jsonify(response), 201
    return jsonify(validator.errors), 400

@category_controller.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    validator = CategoryValidator(data)
    if validator.is_valid():
        service = CategoryService()
        response = service.update_category(category_id, data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400