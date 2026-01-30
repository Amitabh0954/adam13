# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

delete_product_bp = Blueprint('delete_product', __name__)
product_service = ProductService()

@delete_product_bp.route('/delete-product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    data = request.get_json()
    confirmation = data.get('confirmation')

    if confirmation != 'CONFIRM':
        return jsonify({"error": "Delete confirmation required"}), 400

    response = product_service.delete_product(product_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200