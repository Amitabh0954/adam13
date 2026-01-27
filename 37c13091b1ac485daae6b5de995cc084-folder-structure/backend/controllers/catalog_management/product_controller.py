from flask import Blueprint, request, jsonify
from backend.services.catalog_management.product_service import ProductService
from flask_login import login_required, current_user

product_blueprint = Blueprint('product', __name__)
product_service = ProductService()

# Inline comment referencing the Epic Title
# Epic Title: Shopping Cart Functionality

@product_blueprint.route('/products', methods=['POST'])
@login_required
def add_product():
    data = request.get_json()
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        product = product_service.add_product(data)
        return jsonify(product), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    data = request.get_json()
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        product = product_service.update_product(product_id, data)
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        product_service.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    try:
        results, total = product_service.search_products(query, page, per_page)
        return jsonify({
            "results": results,
            "total": total,
            "page": page,
            "per_page": per_page
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400