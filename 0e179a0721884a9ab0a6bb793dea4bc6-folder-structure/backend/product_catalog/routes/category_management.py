# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.category_service import CategoryService
from flask_login import login_required

category_management_bp = Blueprint('category_management', __name__)
category_service = CategoryService()

@category_management_bp.route('/category', methods=['POST'])
@login_required
def add_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    response = category_service.add_category(name, parent_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 201

@category_management_bp.route('/category/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    response = category_service.delete_category(category_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@category_management_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = category_service.get_all_categories()
    return jsonify(categories), 200