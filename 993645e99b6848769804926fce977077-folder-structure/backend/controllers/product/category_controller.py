from flask import Blueprint, request, jsonify
from backend.services.product.category_service import CategoryService
from flask_login import login_required, current_user
import logging

logger = logging.getLogger(__name__)
category_bp = Blueprint('category', __name__)

category_service = CategoryService()

@category_bp.route('/category', methods=['POST'])
@login_required
def add_category():
    if not current_user.is_admin:
        logger.warning(f"Unauthorized add category attempt by user_id: {current_user.id}")
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        logger.warning("Category name is required")
        return jsonify({"message": "Category name is required"}), 400

    try:
        category_service.add_category(name, parent_id)
        logger.info(f"Category added with name: {name}")
        return jsonify({"message": "Category added successfully"}), 201
    except ValueError as e:
        logger.warning(f"Adding category failed: {str(e)}")
        return jsonify({"message": str(e)}), 400

@category_bp.route('/category/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    if not current_user.is_admin:
        logger.warning(f"Unauthorized delete category attempt by user_id: {current_user.id}")
        return jsonify({"message": "Unauthorized"}), 403
    
    try:
        category_service.delete_category(category_id)
        logger.info(f"Category deleted: {category_id}")
        return jsonify({"message": "Category deleted successfully"}), 200
    except ValueError as e:
        logger.warning(f"Deleting category failed: {str(e)}")
        return jsonify({"message": str(e)}), 400