from flask import Blueprint, request, jsonify
from backend.services.catalog_management.category_service import CategoryService
from flask_login import login_required, current_user

category_blueprint = Blueprint('category', __name__)
category_service = CategoryService()

# Inline comment referencing the Epic Title
# Epic Title: Product Catalog Management

@category_blueprint.route('/categories', methods=['POST'])
@login_required
def add_category():
    data = request.get_json()
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        category = category_service.add_category(data)
        return jsonify(category), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
@login_required
def update_category(category_id):
    data = request.get_json()
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        category = category_service.update_category(category_id, data)
        return jsonify(category), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        category_service.delete_category(category_id)
        return jsonify({"message": "Category deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400