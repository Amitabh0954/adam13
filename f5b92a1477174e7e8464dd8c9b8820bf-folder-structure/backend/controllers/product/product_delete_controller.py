from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product.product_delete_service import ProductDeleteService
import logging

logger = logging.getLogger(__name__)
product_delete_bp = Blueprint('product_delete', __name__)

product_delete_service = ProductDeleteService()

@product_delete_bp.route('/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        logger.warning("Non-admin user tried to delete product")
        return jsonify({"message": "Admins only"}), 403

    confirmation = request.args.get('confirmation', 'no')

    if confirmation.lower() != 'yes':
        logger.warning("Product deletion requested without confirmation")
        return jsonify({"message": "Please confirm deletion"}), 400

    try:
        product_delete_service.delete_product(product_id)
        logger.info(f"Product {product_id} deleted successfully")
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        logger.warning(f"Deleting product failed: {str(e)}")
        return jsonify({"message": str(e)}), 400