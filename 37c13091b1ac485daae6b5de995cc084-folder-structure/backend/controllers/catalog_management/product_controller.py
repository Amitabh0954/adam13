from flask import Blueprint, request, jsonify
from backend.services.catalog_management.product_service import ProductService
from flask_login import login_required, current_user

product_blueprint = Blueprint('product', __name__)
product_service = ProductService()

@product_blueprint.route('/products', methods=['POST'])
@login_required
def add_product():
    data = request.get_json()
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        product = product_service.add_product(data)
        return jsonify(product), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400