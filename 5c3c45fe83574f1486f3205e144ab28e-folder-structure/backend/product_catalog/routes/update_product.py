# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.update_product_service import UpdateProductService

update_product_bp = Blueprint('update_product', __name__)

@update_product_bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product_service = UpdateProductService()
    response = product_service.update_product(product_id, data)
    if response.get("error"):
        return jsonify(response), 400
    return jsonify(response), 200