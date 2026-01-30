# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService
from flask_login import login_required

update_product_bp = Blueprint('update_product', __name__)
product_service = ProductService()

@update_product_bp.route('/product/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if price is not None and not isinstance(price, (int, float)):
        return jsonify({"error": "Price must be a numeric value"}), 400

    if description is not None and not description.strip():
        return jsonify({"error": "Description cannot be empty"}), 400

    response = product_service.update_product(product_id, name, price, description)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200