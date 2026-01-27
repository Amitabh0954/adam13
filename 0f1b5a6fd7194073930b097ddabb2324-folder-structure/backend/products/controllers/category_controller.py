from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.products.models.category import Category
from backend.products.repositories.category_repository import CategoryRepository

category_blueprint = Blueprint('category', __name__)
category_repository = CategoryRepository()

@category_blueprint.route('/categories', methods=['POST'])
@login_required
def create_category():
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can create categories"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    category = category_repository.create_category(name, parent_id)
    return jsonify({"message": "Category created successfully", "category": category.to_dict()}), 201

@category_blueprint.route('/categories', methods=['GET'])
def get_categories():
    categories = category_repository.get_all_categories()
    category_list = [category.to_dict() for category in categories]
    return jsonify({"categories": category_list}), 200

@category_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
@login_required
def update_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can update categories"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    category = category_repository.get_category_by_id(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    category.name = name if name else category.name
    category.parent_id = parent_id if parent_id else category.parent_id
    updated_category = category_repository.update_category(category)
    return jsonify({"message": "Category updated successfully", "category": updated_category.to_dict()}), 200

@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can delete categories"}), 403

    category_repository.delete_category(category_id)
    return jsonify({"message": "Category deleted successfully"}), 200