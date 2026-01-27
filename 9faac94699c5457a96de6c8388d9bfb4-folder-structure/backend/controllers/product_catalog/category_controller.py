# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.services.product_catalog.category_service import CategoryService

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/categories', methods=['POST'])
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

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    category_service = CategoryService()
    categories = category_service.get_categories()
    return jsonify(categories), 200