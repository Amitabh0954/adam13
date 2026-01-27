# Epic Title: Product Catalog Management

from flask import Blueprint, jsonify, request
from backend.services.product_catalog.product_delete_service import ProductDeleteService

product_delete_bp = Blueprint('product_delete_bp', __name__)

@product_delete_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    confirmation = request.json.get('confirmation')
    if not confirmation or confirmation.lower() != 'yes':
        return jsonify({'message': 'Deletion not confirmed'}), 400

    product_delete_service = ProductDeleteService()
    result = product_delete_service.delete_product(product_id)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Product deleted successfully'}), 200