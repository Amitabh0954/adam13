from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product_catalog.product_service import ProductService
import logging

logger = logging.getLogger(__name__)
product_update_bp = Blueprint('product_update', __name__)

product_service = ProductService()

@product_update_bp.route('/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    if not current_user.is_admin:
        logger.warning("Non-admin user tried to update a product")
        return jsonify({"message": "Admins only"}), 403

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if price is not None and price <= 0:
        logger.warning("Price must be a positive number")
        return jsonify({"message": "Price must be a positive number"}), 400

    if description is not None and not description:
        logger.warning("Description cannot be empty")
        return jsonify({"message": "Description cannot be empty"}), 400

    try:
        product_service.update_product(product_id, name, price, description)
        logger.info(f"Product '{name}' updated successfully")
        return jsonify({"message": "Product updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Failed to update product: {str(e)}")
        return jsonify({"message": str(e)}), 400