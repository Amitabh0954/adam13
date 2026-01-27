from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.catalog_management.product_service import ProductService

product_blueprint = Blueprint('product', __name__)
product_service = ProductService()

@product_blueprint.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        product = product_service.add_product(data)
        return jsonify(product), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id: int):
    data = request.get_json()
    try:
        product = product_service.update_product(current_user, product_id, data)
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id: int):
    try:
        product_service.delete_product(current_user, product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/search', methods=['GET'])
def search_products():
    term = request.args.get('term', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    products = product_service.search_products(term, page, per_page)
    return jsonify(products), 200