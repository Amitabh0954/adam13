from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.catalog_management.product_service import ProductService

product_blueprint = Blueprint('product', __name__)
product_service = ProductService()

@product_blueprint.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        product = product_service.add_product(data)
        return jsonify(product), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id: int):
    data = request.get_json()
    try:
        product = product_service.update_product(current_user, product_id, data) 
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400