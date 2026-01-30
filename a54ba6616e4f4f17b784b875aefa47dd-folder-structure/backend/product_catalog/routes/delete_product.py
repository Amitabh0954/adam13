# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

delete_product_bp = Blueprint('delete_product', __name__)
product_service = ProductService()

@delete_product_bp.route('/delete', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    product_id = data.get('product_id')
    admin_auth = request.headers.get('Authorization')
    
    if not admin_auth or admin_auth != 'Bearer admin-token':
        return jsonify({"error": "Admin privileges required"}), 403
    
    response = product_service.delete_product(product_id)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200