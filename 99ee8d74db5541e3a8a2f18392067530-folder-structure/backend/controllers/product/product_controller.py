# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
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