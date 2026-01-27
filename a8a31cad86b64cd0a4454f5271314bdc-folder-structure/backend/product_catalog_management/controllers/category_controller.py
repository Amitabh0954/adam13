# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.product_catalog_management.services.category_service import CategoryService
from backend.auth.decorators import admin_required

category_bp = Blueprint('category_bp', __name__)
category_service = CategoryService()

@category_bp.route('/add', methods=['POST'])
@admin_required
def add_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'message': 'Category name is required'}), 400

    result = category_service.add_category(name, parent_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category added successfully'}), 201

@category_bp.route('/<int:category_id>', methods=['PUT'])
@admin_required
def update_category(category_id):
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'message': 'Category name is required'}), 400

    result = category_service.update_category(category_id, name, parent_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category updated successfully'}), 200

@category_bp.route('/<int:category_id>', methods=['DELETE'])
@admin_required
def delete_category(category_id):
    result = category_service.delete_category(category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category deleted successfully'}), 200