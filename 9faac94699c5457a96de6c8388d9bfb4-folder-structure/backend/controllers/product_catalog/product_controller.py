# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or price is None:
        return jsonify({'message': 'Name, description, and price are required'}), 400

    product_service = ProductService()
    result = product_service.add_product(name, description, price)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product added successfully'}), 201