from flask import Blueprint, request, jsonify
from backend.services.product.product_service import ProductService
from flask_login import login_required, current_user
import logging

logger = logging.getLogger(__name__)
product_bp = Blueprint('product', __name__)

product_service = ProductService()

@product_bp.route('/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    if not current_user.is_admin:
        logger.warning(f"Unauthorized update attempt by user_id: {current_user.id}")
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    try:
        product_service.update_product(product_id, name, price, description)
        logger.info(f"Product updated: {product_id}")
        return jsonify({"message": "Product updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Product update failed: {str(e)}")
        return jsonify({"message": str(e)}), 400