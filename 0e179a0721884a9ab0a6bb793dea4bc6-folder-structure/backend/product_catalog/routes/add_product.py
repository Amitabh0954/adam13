# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

add_product_bp = Blueprint('add_product', __name__)
product_service = ProductService()

@add_product_bp.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if not name or not price or not description:
        return jsonify({"error": "Name, price, and description are required"}), 400

    response = product_service.add_product(name, price, description)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 201