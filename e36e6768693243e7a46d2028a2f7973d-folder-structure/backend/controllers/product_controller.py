# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.services.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if not name or not description or price is None:
        return jsonify({'message': 'Name, description, and price are required'}), 400

    product_service = ProductService()
    result = product_service.add_product(name, description, price, category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product added successfully'}), 201

@product_bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    product_service = ProductService()
    result = product_service.update_product(product_id, name, description, price, category_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product updated successfully'}), 200

@product_bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    product_service = ProductService()
    result = product_service.delete_product(product_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product deleted successfully'}), 200

@product_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    product_service = ProductService()
    results = product_service.search_products(query, page, per_page)
    return jsonify(results), 200