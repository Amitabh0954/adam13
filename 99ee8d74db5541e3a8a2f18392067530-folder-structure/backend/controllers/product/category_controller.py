# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify, session
from backend.services.product.category_service import CategoryService

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/add', methods=['POST'])
def add_category():
    if not session.get('is_admin'):
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'message': 'Category name is required'}), 400

    category_service = CategoryService()
    result = category_service.add_category(name, parent_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category added successfully'}), 201

@category_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    if not session.get('is_admin'):
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    category_service = CategoryService()
    result = category_service.update_category(category_id, name, parent_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category updated successfully'}), 200

@category_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    if not session.get('is_admin'):
        return jsonify({'message': 'Admin access required'}), 403

    category_service = CategoryService()
    result = category_service.delete_category(category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category deleted successfully'}), 200