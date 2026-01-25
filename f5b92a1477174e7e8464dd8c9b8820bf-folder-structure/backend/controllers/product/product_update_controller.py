from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product.product_update_service import ProductUpdateService
import logging

logger = logging.getLogger(__name__)
product_update_bp = Blueprint('product_update', __name__)

product_update_service = ProductUpdateService()

@product_update_bp.route('/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    if not current_user.is_admin:
        logger.warning("Non-admin user tried to update product")
        return jsonify({"message": "Admins only"}), 403

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if name is None or price is None or description is None:
        logger.warning("Name, price, and description are required to update a product")
        return jsonify({"message": "Name, price, and description are required"}), 400

    if not isinstance(price, (int, float)) or price < 0:
        logger.warning("Price must be a positive number")
        return jsonify({"message": "Price must be a positive number"}), 400

    try:
        product_update_service.update_product(product_id, name, price, description)
        logger.info(f"Product {product_id} updated successfully")
        return jsonify({"message": "Product updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Updating product failed: {str(e)}")
        return jsonify({"message": str(e)}), 400