# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

update_product_bp = Blueprint('update_product', __name__)
product_service = ProductService()

@update_product_bp.route('/update', methods=['PUT'])
def update_product():
    data = request.get_json()
    product_id = data.get('product_id')
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    admin_auth = request.headers.get('Authorization')
    
    if not admin_auth or admin_auth != 'Bearer admin-token':
        return jsonify({"error": "Admin privileges required"}), 403
    
    response = product_service.update_product(product_id, name, price, description)
    
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200