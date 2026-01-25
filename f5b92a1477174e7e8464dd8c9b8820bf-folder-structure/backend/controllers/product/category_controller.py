from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product.category_service import CategoryService
import logging

logger = logging.getLogger(__name__)
category_bp = Blueprint('category', __name__)

category_service = CategoryService()

@category_bp.route('/categories', methods=['POST'])
@login_required
def create_category():
    if not current_user.is_admin:
        logger.warning("Non-admin user tried to create category")
        return jsonify({"message": "Admins only"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        logger.warning("Category name is required")
        return jsonify({"message": "Category name is required"}), 400

    try:
        category = category_service.create_category(name, parent_id)
        logger.info(f"Category '{name}' created with ID {category.id}")
        return jsonify({"message": "Category created", "category": category.to_dict()}), 201
    except ValueError as e:
        logger.warning(f"Category creation failed: {str(e)}")
        return jsonify({"message": str(e)}), 400