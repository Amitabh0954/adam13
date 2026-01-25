from flask import Blueprint, request, jsonify
from backend.services.product.product_service import ProductService
from flask_login import login_required, current_user
import logging

logger = logging.getLogger(__name__)
product_bp = Blueprint('product', __name__)

product_service = ProductService()

@product_bp.route('/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        logger.warning(f"Unauthorized delete attempt by user_id: {current_user.id}")
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json()
    confirmation = data.get('confirmation')

    if confirmation != "CONFIRM":
        logger.warning(f"Delete attempt without confirmation by user_id: {current_user.id}")
        return jsonify({"message": "Delete action not confirmed"}), 400

    try:
        product_service.delete_product(product_id)
        logger.info(f"Product deleted: {product_id}")
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        logger.warning(f"Product deletion failed: {str(e)}")
        return jsonify({"message": str(e)}), 400