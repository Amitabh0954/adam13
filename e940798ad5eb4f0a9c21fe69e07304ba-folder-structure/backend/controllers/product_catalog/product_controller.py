# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_service import ProductService

product_bp = Blueprint('product', __name__)
product_service = ProductService()

@product_bp.route('/api/product_catalog/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if not name or not description or price is None or category_id is None:
        return jsonify({"error": "Name, description, price, and category_id are required"}), 400

    response = product_service.add_product(name, description, price, category_id)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200