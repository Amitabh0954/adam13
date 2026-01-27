from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.catalog_management.category_service import CategoryService

category_blueprint = Blueprint('category', __name__)
category_service = CategoryService()

@category_blueprint.route('/categories', methods=['POST'])
@login_required
def add_category():
    data = request.get_json()
    try:
        category = category_service.add_category(data)
        return jsonify(category), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
@login_required
def update_category(category_id: int):
    data = request.get_json()
    try:
        category = category_service.update_category(category_id, data)
        return jsonify(category), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id: int):
    try:
        category_service.delete_category(category_id)
        return jsonify({"message": "Category deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400