from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.repositories.product_catalog.category_repository import CategoryRepository

category_controller = Blueprint('category_controller', __name__)
category_repository = CategoryRepository()

@category_controller.route('/categories', methods=['POST'])
@login_required
def create_category():
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can create categories"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if name is None or name == "":
        return jsonify({"error": "Category name is required"}), 400

    if category_repository.get_category_by_name(name):
        return jsonify({"error": "Category name must be unique"}), 400

    parent = None
    if parent_id:
        parent = category_repository.get_category_by_id(parent_id)
        if parent is None:
            return jsonify({"error": "Parent category not found"}), 404

    new_category = category_repository.create_category(name, parent)
    return jsonify({"message": "Category created successfully"}), 201

@category_controller.route('/categories', methods=['GET'])
def get_categories():
    categories = category_repository.get_all_categories()
    all_categories = [{
        "id": category.id,
        "name": category.name,
        "parent_id": category.parent_id
    } for category in categories]

    return jsonify({"categories": all_categories}), 200

@category_controller.route('/categories/<int:category_id>', methods=['PUT'])
@login_required
def update_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can update categories"}), 403
    
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    category = category_repository.get_category_by_id(category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404

    if name:
        if category_repository.get_category_by_name(name):
            return jsonify({"error": "Category name must be unique"}), 400
        category.name = name

    if parent_id is not None:
        parent = category_repository.get_category_by_id(parent_id)
        if parent is None:
            return jsonify({"error": "Parent category not found"}), 404
        category.parent = parent

    category_repository.update_category(category)
    return jsonify({"message": "Category updated successfully"}), 200

@category_controller.route('/categories/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can delete categories"}), 403

    category = category_repository.get_category_by_id(category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404

    category_repository.delete_category(category)
    return jsonify({"message": "Category deleted successfully"}), 200