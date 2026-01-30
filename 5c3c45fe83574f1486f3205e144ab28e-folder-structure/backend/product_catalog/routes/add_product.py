# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.add_product_service import AddProductService

add_product_bp = Blueprint('add_product', __name__)

@add_product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    product_service = AddProductService()
    response = product_service.add_product(data)
    if response.get("error"):
        return jsonify(response), 400
    return jsonify(response), 201