# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_update_service import ProductUpdateService

product_update_bp = Blueprint('product_update_bp', __name__)

@product_update_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if price is not None and (not isinstance(price, (int, float)) or price <= 0):
        return jsonify({'message': 'Price must be a positive numeric value'}), 400

    if description == "":
        return jsonify({'message': 'Description cannot be removed'}), 400

    product_update_service = ProductUpdateService()
    result = product_update_service.update_product(product_id, name, description, price)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product updated successfully'}), 200