# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

update_product_bp = Blueprint('update_product', __name__)
product_service = ProductService()

@update_product_bp.route('/update-product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description', None)

    if not name or not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Name, valid numeric price, and non-empty description are required"}), 400

    response = product_service.update_product(product_id, name, price, description)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200