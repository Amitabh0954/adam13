# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify, session
from backend.services.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_id = data.get('category_id')

    if not name or not price or not description or not category_id:
        return jsonify({'message': 'All fields are required'}), 400

    product_service = ProductService()
    result = product_service.add_product(name, price, description, category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product added successfully'}), 201

@product_bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if not session.get('is_admin'):
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_id = data.get('category_id')

    if price is not None and not isinstance(price, (int, float)):
        return jsonify({'message': 'Price must be a numeric value'}), 400

    product_service = ProductService()
    result = product_service.update_product(product_id, name, price, description, category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product updated successfully'}), 200

@product_bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if not session.get('is_admin'):
        return jsonify({'message': 'Admin access required'}), 403

    product_service = ProductService()
    result = product_service.delete_product(product_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product deleted successfully'}), 200