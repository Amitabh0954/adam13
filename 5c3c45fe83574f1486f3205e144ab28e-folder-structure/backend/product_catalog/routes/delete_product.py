# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.delete_product_service import DeleteProductService

delete_product_bp = Blueprint('delete_product', __name__)

@delete_product_bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    data = request.get_json()
    admin_confirmation = data.get('admin_confirmation')
    if not admin_confirmation:
        return jsonify({"error": "Delete confirmation required"}), 400
    
    product_service = DeleteProductService()
    response = product_service.delete_product(product_id)
    
    if response.get("error"):
        return jsonify(response), 400
        
    return jsonify(response), 200