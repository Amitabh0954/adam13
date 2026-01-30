# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from backend.services.product_catalog.category_service import CategoryService

category_bp = Blueprint('category', __name__)
category_service = CategoryService()

@category_bp.route('/api/product_catalog/add_category', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    parent_id = data.get('parent_id')

    if not name or not description:
        return jsonify({"error": "Name and description are required"}), 400

    response = category_service.add_category(name, description, parent_id)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200

@category_bp.route('/api/product_catalog/categories', methods=['GET'])
def get_all_categories():
    categories = category_service.get_all_categories()
    return jsonify(categories), 200