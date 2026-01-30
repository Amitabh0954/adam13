# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_update_service import ProductUpdateService

product_update_bp = Blueprint('product_update', __name__)
product_update_service = ProductUpdateService()

@product_update_bp.route('/api/product_catalog/update_product', methods=['PUT'])
def update_product():
    data = request.get_json()
    product_id = data.get('product_id')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if not product_id or not name or price is None or category_id is None:
        return jsonify({"error": "Product ID, name, price, and category_id are required"}), 400

    response = product_update_service.update_product(product_id, name, description, price, category_id)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200