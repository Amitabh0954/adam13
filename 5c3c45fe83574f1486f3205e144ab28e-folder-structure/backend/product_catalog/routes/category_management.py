# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.category_management_service import CategoryManagementService

category_management_bp = Blueprint('category_management', __name__)
category_service = CategoryManagementService()

@category_management_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = category_service.get_all_categories()
    return jsonify(categories), 200

@category_management_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    response = category_service.create_category(data)
    if response.get("error"):
        return jsonify(response), 400
    return jsonify(response), 201

@category_management_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    response = category_service.update_category(category_id, data)
    if response.get("error"):
        return jsonify(response), 400
    return jsonify(response), 200