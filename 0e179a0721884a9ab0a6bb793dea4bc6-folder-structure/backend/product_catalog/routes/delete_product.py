# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService
from flask_login import login_required

delete_product_bp = Blueprint('delete_product', __name__)
product_service = ProductService()

@delete_product_bp.route('/product/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    confirmation = request.args.get('confirmation')

    if confirmation != 'true':
        return jsonify({"error": "Confirmation is required to delete a product"}), 400

    response = product_service.delete_product(product_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200