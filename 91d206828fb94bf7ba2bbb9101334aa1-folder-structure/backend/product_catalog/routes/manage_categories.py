# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.category_service import CategoryService

manage_categories_bp = Blueprint('manage_categories', __name__)
category_service = CategoryService()

@manage_categories_bp.route('/categories', methods=['POST'])
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

@manage_categories_bp.route('/categories', methods=['GET'])
def get_categories():
    response = category_service.get_categories()
    return jsonify(response), 200

@manage_categories_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    response = category_service.delete_category(category_id)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200