# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.services.category_service import CategoryService

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/add', methods=['POST'])
def add_category():
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

@category_bp.route('/update/<int:category_id>', methods=['PUT'])
def update_category(category_id: int):
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    category_service = CategoryService()
    result = category_service.update_category(category_id, name, parent_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category updated successfully'}), 200

@category_bp.route('/delete/<int:category_id>', methods=['DELETE'])
def delete_category(category_id: int):
    category_service = CategoryService()
    result = category_service.delete_category(category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Category deleted successfully'}), 200