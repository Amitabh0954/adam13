from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product_catalog.product_service import ProductService
import logging

logger = logging.getLogger(__name__)
product_delete_bp = Blueprint('product_delete', __name__)

product_service = ProductService()

@product_delete_bp.route('/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        logger.warning("Non-admin user tried to delete a product")
        return jsonify({"message": "Admins only"}), 403

    try:
        product_service.delete_product(product_id)
        logger.info(f"Product with ID '{product_id}' deleted successfully")
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        logger.warning(f"Failed to delete product: {str(e)}")
        return jsonify({"message": str(e)}), 400