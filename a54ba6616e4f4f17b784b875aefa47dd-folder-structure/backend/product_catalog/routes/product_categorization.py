# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.category_service import CategoryService

product_categorization_bp = Blueprint('product_categorization', __name__)
category_service = CategoryService()

@product_categorization_bp.route('/add_category', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')
    admin_auth = request.headers.get('Authorization')

    if not admin_auth or admin_auth != 'Bearer admin-token':
        return jsonify({"error": "Admin privileges required"}), 403

    response = category_service.add_category(name, parent_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 201

@product_categorization_bp.route('/assign_category', methods=['POST'])
def assign_category():
    data = request.get_json()
    product_id = data.get('product_id')
    category_id = data.get('category_id')
    admin_auth = request.headers.get('Authorization')

    if not admin_auth or admin_auth != 'Bearer admin-token':
        return jsonify({"error": "Admin privileges required"}), 403

    response = category_service.assign_category(product_id, category_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200