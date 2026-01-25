from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product_catalog.category_service import CategoryService
import logging

logger = logging.getLogger(__name__)
category_bp = Blueprint('category', __name__)

category_service = CategoryService()

@category_bp.route('/categories', methods=['POST'])
@login_required
def add_category():
    if not current_user.is_admin:
        logger.warning("Unauthorized access attempt by user")
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        logger.warning("Category name is required")
        return jsonify({"message": "Category name is required"}), 400

    try:
        category_service.add_category(name, parent_id)
        logger.info(f"Category '{name}' added successfully")
        return jsonify({"message": "Category added successfully"}), 201
    except ValueError as e:
        logger.warning(f"Failed to add category: {str(e)}")
        return jsonify({"message": str(e)}), 400

@category_bp.route('/categories/<int:category_id>', methods=['PATCH'])
@login_required
def update_category(category_id: int):
    if not current_user.is_admin:
        logger.warning("Unauthorized access attempt by user")
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    try:
        category_service.update_category(category_id, name, parent_id)
        logger.info(f"Category '{name}' updated successfully")
        return jsonify({"message": "Category updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Failed to update category: {str(e)}")
        return jsonify({"message": str(e)}), 400