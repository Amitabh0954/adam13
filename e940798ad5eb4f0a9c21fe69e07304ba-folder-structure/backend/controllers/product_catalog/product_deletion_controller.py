# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_deletion_service import ProductDeletionService

product_deletion_bp = Blueprint('product_deletion', __name__)
product_deletion_service = ProductDeletionService()

@product_deletion_bp.route('/api/product_catalog/delete_product', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    product_id = data.get('product_id')
    confirmation = data.get('confirmation')

    if not product_id or not confirmation:
        return jsonify({"error": "Product ID and confirmation are required"}), 400

    if confirmation != "YES":
        return jsonify({"error": "Deletion not confirmed"}), 400

    response = product_deletion_service.delete_product(product_id)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200