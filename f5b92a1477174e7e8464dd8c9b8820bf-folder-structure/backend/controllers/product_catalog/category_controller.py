from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.product_catalog.category_service import CategoryService
import logging

logger = logging.getLogger(__name__)
category_bp = Blueprint('category', __name__)

category_service = CategoryService()

@category_bp.route('/categories', methods=['GET'])
def get_all_categories():
    categories = category_service.get_all_categories()
    return jsonify(categories), 200

@category_bp.route('/categories', methods=['POST'])
@login_required
def add_category():
    if not current_user.is_admin:
        logger.warning("Non-admin user tried to add a category")
        return jsonify({"message": "Admins only"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        logger.warning("Category name is required")
        return jsonify({"message": "Category name is required"}), 400
    
    try:
        category = category_service.add_category(name, parent_id)
        logger.info(f"Category '{name}' added successfully")
        return jsonify(category), 201
    except ValueError as e:
        logger.warning(f"Failed to add category: {str(e)}")
        return jsonify({"message": str(e)}), 400