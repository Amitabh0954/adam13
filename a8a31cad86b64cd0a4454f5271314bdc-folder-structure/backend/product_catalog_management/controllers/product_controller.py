# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.product_catalog_management.services.product_service import ProductService
from backend.auth.decorators import admin_required

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_id = data.get('category_id')

    if not name or not description or not category_id:
        return jsonify({'message': 'Name, description, and category_id are required'}), 400

    if price is None or price <= 0:
        return jsonify({'message': 'Price must be a positive number'}), 400

    product_service = ProductService()
    result = product_service.add_product(name, description, price, category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product added successfully'}), 201

@product_bp.route('/update/<int:product_id>', methods=['PUT'])
@admin_required
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_id = data.get('category_id')

    if price is not None and price <= 0:
        return jsonify({'message': 'Price must be a positive number'}), 400

    product_service = ProductService()
    result = product_service.update_product(product_id, name, description, price, category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product updated successfully'}), 200

@product_bp.route('/delete/<int:product_id>', methods=['DELETE'])
@admin_required
def delete_product(product_id):
    confirm = request.args.get('confirm')

    if confirm != 'true':
        return jsonify({'message': 'Confirmation required to delete this product. Add ?confirm=true to the request.'}), 403

    product_service = ProductService()
    result = product_service.delete_product(product_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product deleted successfully'}), 200